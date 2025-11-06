from __future__ import annotations
from pathlib import Path
from moviepy.editor import VideoFileClip
import subprocess

def extract_audio(input_path: str | Path, output_path: str | Path, sample_rate: int = 16000) -> Path:
    input_path = Path(input_path)
    output_path = Path(output_path)
    # escolher extensão wav
    if output_path.suffix.lower() != ".wav":
        output_path = output_path.with_suffix(".wav")

    try:
        video = VideoFileClip(str(input_path))
        audio = video.audio
        audio.write_audiofile(str(output_path), verbose=False, logger=None)
        audio.close(); video.close()
        return output_path
    except Exception as e:
        print(f"[extractor] MoviePy falhou ({e}), usando ffmpeg...")
        cmd = [
            "ffmpeg", "-y", "-i", str(input_path), "-vn",
            "-acodec", "pcm_s16le", "-ar", str(sample_rate), "-ac", "1",
            str(output_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg falhou: {result.stderr[:500]}")
        return output_path