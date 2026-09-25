from __future__ import annotations
import argparse
from pathlib import Path
from .config import TranscriberConfig
from .transcribe import transcribe_file


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Transcritor de Áudio/Vídeo de Alta Performance (faster-whisper + CUDA)")
    p.add_argument("input", help="Arquivo de áudio/vídeo a transcrever")
    p.add_argument("-o", "--output", help="Arquivo de saída (padrão: <input>.txt)")
    p.add_argument("-m", "--model", default="base", 
                   choices=["tiny", "tiny.en", "base", "base.en", "small", "small.en", "medium", "medium.en", "large-v1", "large-v2", "large-v3", "large", "distil-large-v3"], 
                   help="Tamanho do modelo Whisper (padrão: base)")
    p.add_argument("-l", "--language", default="pt", 
                   help="Idioma: pt, en, es, auto, etc. (padrão: pt)")
    p.add_argument("-c", "--compute-type", default=None,
                   choices=["float16", "int8_float16", "int8", "float32", "auto"],
                   help="Tipo de precisão de cálculo (padrão: float16 em GPU, int8 em CPU)")
    p.add_argument("--no-cuda", action="store_true", 
                   help="Desabilitar CUDA (força uso de CPU)")
    p.add_argument("--no-timestamps", action="store_true", 
                   help="Não incluir timestamps na transcrição")
    p.add_argument("--no-vad", action="store_true",
                   help="Desativar filtro de atividade de voz (Silero VAD)")
    return p


def main(argv: list[str] | None = None):
    parser = build_parser()
    args = parser.parse_args(argv)

    cfg = TranscriberConfig(
        model_size=args.model,
        language=args.language,
        use_cuda=not args.no_cuda,
        timestamps=not args.no_timestamps,
        compute_type=args.compute_type,
        vad_filter=not args.no_vad,
        output=Path(args.output) if args.output else None,
    ).resolve()

    output = transcribe_file(args.input, cfg)
    print(f"\n Transcrição concluída! Arquivo salvo em: {output}")

if __name__ == "__main__":  # pragma: no cover
    main()