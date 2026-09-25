from __future__ import annotations
from faster_whisper import WhisperModel
import torch
from functools import lru_cache

@lru_cache(maxsize=2)
def load_model(size: str, device: str | None = None, compute_type: str = "default"):
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[model] Carregando modelo faster-whisper '{size}' em {device} (compute_type={compute_type}) ...")
    model = WhisperModel(size, device=device, compute_type=compute_type)
    print("[model] Modelo carregado com sucesso")
    return model