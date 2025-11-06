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
    Transcreve um arquivo de áudio/vídeo para texto.
    
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
    if ext in VIDEO_EXT:
        print(f"[transcribe] Extraindo áudio de vídeo...")
        temp_audio = input_path.with_suffix(".wav")
        audio_to_process = extract_audio(input_path, temp_audio)
    elif ext in AUDIO_EXT:
        audio_to_process = input_path
    else:
        raise ValueError(f"Formato não suportado: {ext}")
    
    # Carrega modelo
    device = "cuda" if config.use_cuda and torch.cuda.is_available() else "cpu"
    model = load_model(config.model_size, device)
    
    # Informações do dispositivo
    device_name = ""
    if device == "cuda":
        device_name = f" ({torch.cuda.get_device_name(0)})"
    
    # Transcreve
    print(f"[transcribe] Transcrevendo '{input_path.name}'")
    print(f"[transcribe] Dispositivo: {device.upper()}{device_name} | Modelo: {config.model_size} | Idioma: {config.language}")
    
    start = time.time()
    result = model.transcribe(
        str(audio_to_process), 
        language=config.language, 
        fp16=config.fp16
    )
    duration = time.time() - start
    
    print(f"[transcribe] Concluído em {duration:.2f}s")
    
    # Salva resultado
    with open(output_path, 'w', encoding='utf-8') as f:
        if config.timestamps and 'segments' in result:
            f.write("=== TRANSCRIÇÃO COM TIMESTAMPS ===\n\n")
            for segment in result['segments']:
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text'].strip()
                f.write(f"[{start_time:.2f}s - {end_time:.2f}s] {text}\n")
            f.write("\n=== TEXTO COMPLETO ===\n\n")
        
        f.write(result['text'])
    
    # Remove arquivo temporário de áudio se foi extraído
    if ext in VIDEO_EXT and audio_to_process.exists():
        audio_to_process.unlink()
    
    print(f"[transcribe] Salvo em: {output_path}")
    return output_path
