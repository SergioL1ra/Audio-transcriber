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
    compute_type: str | None = None
    vad_filter: bool = True

    def resolve(self):
        import torch
        if self.use_cuda and not torch.cuda.is_available():
            self.use_cuda = False

        if self.compute_type is None or self.compute_type == "auto":
            self.compute_type = "float16" if self.use_cuda else "int8"
        elif not self.use_cuda and self.compute_type in ("float16", "int8_float16"):
            self.compute_type = "int8"
        return self