# Transcritor de Áudio (Faster-Whisper)

Transcritor de alta performance para áudio e vídeo usando **Faster-Whisper** (CTranslate2) otimizado para GPUs NVIDIA RTX com aceleração por CUDA e Tensor Cores.

## 🚀 Funcionalidades & Destaques

- **Desempenho Extremo**: Até **4x a 8x mais rápido** que o `openai-whisper` padrão com menor uso de VRAM.
- **Filtro de Atividade de Voz (Silero VAD)**: Remove automaticamente trechos de silêncio, prevenindo alucinações de texto e acelerando o processamento.
- **Suporte a Quantização**: `float16`, `int8_float16`, `int8` para otimização de velocidade em GPUs RTX.
- **Modelos Diversos**: `tiny`, `base`, `small`, `medium`, `large-v2`, `large-v3`, `distil-large-v3`.
- **Aceleração CUDA**: Suporte total a GPUs NVIDIA.
- **Múltiplos Formatos**: MP3, WAV, MP4, M4A, FLAC, OGG, AVI, MOV, MKV.
- **Timestamps Automáticos**: Marcação precisa de tempo para cada segmento transcrito.

## 📋 Requisitos

- Python 3.8+
- GPU NVIDIA com suporte CUDA (recomendado para alta velocidade)
- FFmpeg (para extração de áudio de vídeos)

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/transcritor-audios.git
cd transcritor-audios
```

### 2. Instale as dependências

#### Instalação recomendada (via script):
```bash
python install_dependencies.py
```

#### Instalação manual (PyTorch com CUDA 12.1 + dependências):
```bash
pip install torch torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

---

## 💻 Uso e Exemplos

```bash
# Transcrição padrão (modelo base com CUDA e VAD ativado)
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 

# Modelo de alta precisão (large-v3 ou distil-large-v3)
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --model large-v3

# Modelo com quantização int8_float16 para GPUs com pouca VRAM
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --model medium -c int8_float16

# Especificar arquivo de saída
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --output resultado.txt

# Especificar idioma ou detecção automática
$env:PYTHONPATH="src"; python -m transcriber audio.mp3 --language en
$env:PYTHONPATH="src"; python -m transcriber audio.mp3 --language auto

# Sem timestamps
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-timestamps

# Desativar filtro VAD (Silero VAD)
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-vad

# Forçar uso de CPU (sem GPU)
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-cuda
```

---

## ⚙️ Opções da CLI

```text
Uso: python -m transcriber <arquivo> [opções]

Argumentos:
  arquivo                    Arquivo de áudio/vídeo para transcrever

Opções:
  -o, --output FILE          Arquivo de saída (padrão: <input>.txt)
  -m, --model SIZE           Modelo Whisper: base, small, medium, large-v3, distil-large-v3, etc. (padrão: base)
  -l, --language LANG        Idioma: pt, en, es, auto, etc. (padrão: pt)
  -c, --compute-type TYPE    Precisão: float16, int8_float16, int8, float32 (padrão: float16 em GPU)
  --no-cuda                  Desabilitar CUDA (força uso de CPU)
  --no-timestamps            Não incluir timestamps na transcrição
  --no-vad                   Desativar o filtro de atividade de voz (Silero VAD)
  -h, --help                 Mostrar ajuda
```