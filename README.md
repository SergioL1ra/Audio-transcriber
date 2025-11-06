# Transcritor de Áudio

Transcritor simples e eficiente de áudio/vídeo para texto usando OpenAI Whisper com aceleração CUDA/GPU NVIDIA.

## Funcionalidades

- **Transcrição precisa** usando modelos Whisper (tiny, base, small, medium, large)
- **Aceleração CUDA** para processamento rápido em GPUs NVIDIA
- **Múltiplos formatos** - MP3, WAV, MP4, M4A, FLAC, OGG, AVI, MOV, MKV
- **Timestamps automáticos** - marcação de tempo para cada trecho
- **Suporte multilíngue** - português, inglês, espanhol, etc.
- **Interface simples** - linha de comando fácil de usar

## Requisitos

- Python 3.8+
- GPU NVIDIA com CUDA (opcional, para aceleração)
- FFmpeg (para extração de áudio de vídeos)

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/transcritor-audios.git
cd transcritor-audios
```

### 2. Instale as dependências

#### Instalação automátic
```bash
python install_dependencies.py
```


### Comandos Básicos

```bash
# Transcrição simples
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 

# Com modelo de alta qualidade
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --model medium

# Especificar arquivo de saída
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --output resultado.txt

# Especificar idioma
$env:PYTHONPATH="src"; python -m transcriber audio.mp3 --language en

# Sem timestamps
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-timestamps

# Forçar uso de CPU (sem GPU)
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-cuda
```

### Opções Disponíveis

```
Uso: python -m transcriber <arquivo> [opções]

Argumentos:
  arquivo                    Arquivo de áudio/vídeo para transcrever

Opções:
  -o, --output FILE         Arquivo de saída (padrão: <input>.txt)
  -m, --model SIZE          Modelo Whisper: tiny, base, small, medium, large (padrão: base)
  -l, --language LANG       Idioma: pt, en, es, etc. (padrão: pt)
  --no-cuda                 Desabilitar CUDA (força uso de CPU)
  --no-timestamps           Não incluir timestamps na transcrição
  -h, --help                Mostrar ajuda
```