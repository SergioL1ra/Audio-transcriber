from __future__ import annotations
import argparse
from pathlib import Path
from .config import TranscriberConfig
from .transcribe import transcribe_file


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Transcritor de Áudio/Vídeo (Whisper + CUDA)")
    p.add_argument("input", help="Arquivo de áudio/vídeo a transcrever")
    p.add_argument("-o", "--output", help="Arquivo de saída (padrão: <input>.txt)")
    p.add_argument("-m", "--model", default="base", 
                   choices=["tiny","base","small","medium","large"], 
                   help="Tamanho do modelo Whisper (padrão: base)")
    p.add_argument("-l", "--language", default="pt", 
                   help="Idioma (pt, en, es, ...) (padrão: pt)")
    p.add_argument("--no-cuda", action="store_true", 
                   help="Desabilitar CUDA (força uso de CPU)")
    p.add_argument("--no-timestamps", action="store_true", 
                   help="Não incluir timestamps na transcrição")
    return p


def main(argv: list[str] | None = None):
    parser = build_parser()
    args = parser.parse_args(argv)

    cfg = TranscriberConfig(
        model_size=args.model,
        language=args.language,
        use_cuda=not args.no_cuda,
        timestamps=not args.no_timestamps,
        output=Path(args.output) if args.output else None,
    ).resolve()

    output = transcribe_file(args.input, cfg)
    print(f"\n Transcrição concluída! Arquivo salvo em: {output}")

if __name__ == "__main__":  # pragma: no cover
    main()