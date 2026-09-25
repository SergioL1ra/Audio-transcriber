from __future__ import annotations
from pathlib import Path
from .config import TranscriberConfig
from .model import load_model
from .extractor import extract_audio
import time
import torch

AUDIO_EXT = {".mp3", ".wav", ".m4a", ".flac", ".ogg"}
VIDEO_EXT = {".mp4", ".avi", ".mov", ".mkv"}


def transcribe_file(input_path: str | Path, config: TranscriberConfig) -> Path:
    """
    Transcreve um arquivo de áudio/vídeo para texto usando faster-whisper.
    
    Args:
        input_path: Caminho do arquivo de entrada
        config: Configuração da transcrição
        
    Returns:
        Path do arquivo de saída
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")
    
    # Determina o arquivo de saída
    if config.output:
        output_path = config.output
    else:
        output_path = input_path.with_suffix(".txt")
    
    # Extrai áudio se for vídeo
    ext = input_path.suffix.lower()
    temp_extracted: Path | None = None
    
    try:
        if ext in VIDEO_EXT:
            print(f"[transcribe] Extraindo áudio de vídeo...")
            temp_extracted = input_path.with_name(f"{input_path.stem}_temp_extracted.wav")
            audio_to_process = extract_audio(input_path, temp_extracted)
        elif ext in AUDIO_EXT:
            audio_to_process = input_path
        else:
            raise ValueError(f"Formato não suportado: {ext}")
        
        # Carrega modelo faster-whisper
        device = "cuda" if config.use_cuda and torch.cuda.is_available() else "cpu"
        compute_type = config.compute_type or ("float16" if device == "cuda" else "int8")
        model = load_model(config.model_size, device=device, compute_type=compute_type)
        
        # Informações do dispositivo
        device_name = ""
        if device == "cuda":
            device_name = f" ({torch.cuda.get_device_name(0)})"
        
        # Transcreve
        print(f"[transcribe] Transcrevendo '{input_path.name}'")
        print(f"[transcribe] Dispositivo: {device.upper()}{device_name} | Modelo: {config.model_size} | Idioma: {config.language} | Compute: {compute_type} | VAD: {config.vad_filter}")
        
        start = time.time()
        
        lang_param = None if (not config.language or config.language.lower() == "auto") else config.language
        
        segments_gen, info = model.transcribe(
            str(audio_to_process),
            language=lang_param,
            vad_filter=config.vad_filter,
            vad_parameters=dict(min_silence_duration_ms=500) if config.vad_filter else None
        )
        
        # Consome o gerador para obter todos os segmentos
        segments = list(segments_gen)
        duration = time.time() - start
        
        print(f"[transcribe] Concluído em {duration:.2f}s (Duração do áudio: {info.duration:.2f}s | Idioma detectado: {info.language} [{info.language_probability:.2%}])")
        
        # Salva resultado
        with open(output_path, 'w', encoding='utf-8') as f:
            if config.timestamps and segments:
                f.write("=== TRANSCRIÇÃO COM TIMESTAMPS ===\n\n")
                for segment in segments:
                    text = segment.text.strip()
                    f.write(f"[{segment.start:.2f}s - {segment.end:.2f}s] {text}\n")
                f.write("\n=== TEXTO COMPLETO ===\n\n")
                f.write("\n".join(s.text.strip() for s in segments))
            else:
                f.write("\n".join(s.text.strip() for s in segments))
        
        print(f"[transcribe] Salvo em: {output_path}")
        return output_path

    finally:
        # Remove arquivo temporário de áudio se foi extraído
        if temp_extracted and temp_extracted.exists():
            try:
                temp_extracted.unlink()
            except Exception:
                pass
