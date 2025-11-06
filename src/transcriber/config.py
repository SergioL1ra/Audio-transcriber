from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass
class TranscriberConfig:
    model_size: str = "base"
    language: str = "pt"
    use_cuda: bool = True
    timestamps: bool = True
    output: Path | None = None
    fp16: bool | None = None  # auto decide based on cuda

    def resolve(self):
        import torch
        if self.fp16 is None:
            self.fp16 = self.use_cuda and torch.cuda.is_available()
        if self.use_cuda and not torch.cuda.is_available():
            self.use_cuda = False
        return self