from __future__ import annotations
import whisper
import torch
from functools import lru_cache

@lru_cache(maxsize=2)
def load_model(size: str, device: str | None = None):
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[model] Carregando modelo '{size}' em {device} ...")
    model = whisper.load_model(size, device=device)
    print("[model] Modelo carregado")
    return model