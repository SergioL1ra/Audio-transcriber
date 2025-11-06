# Transcritor de Áudio

Transcritor simples e eficiente de áudio/vídeo para texto usando OpenAI Whisper com aceleração CUDA/GPU NVIDIA.

## Funcionalidades

-  **Transcrição precisa** usando modelos Whisper (tiny, base, small, medium, large)
- ⚡ **Aceleração CUDA** para processamento rápido em GPUs NVIDIA
- 🎵 **Múltiplos formatos** - MP3, WAV, MP4, M4A, FLAC, OGG, AVI, MOV, MKV
- 📝 **Timestamps automáticos** - marcação de tempo para cada trecho
- 🌍 **Suporte multilíngue** - português, inglês, espanhol, etc.
- 💻 **Interface simples** - linha de comando fácil de usar

## Requisitos

- Python 3.8+
- GPU NVIDIA com CUDA (opcional, para aceleração)
- FFmpeg (para extração de áudio de vídeos)

## 🚀 Instalação

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

## 🎭 Modelos Whisper

| Modelo | Tamanho | Precisão | Velocidade | Uso Recomendado |
|--------|---------|----------|------------|-----------------|
| **tiny** | 39MB | ⭐⭐ | ⚡⚡⚡⚡ | Testes rápidos |
| **base** | 74MB | ⭐⭐⭐ | ⚡⚡⚡ | Uso geral (padrão) |
| **small** | 244MB | ⭐⭐⭐⭐ | ⚡⚡ | Boa qualidade |
| **medium** | 769MB | ⭐⭐⭐⭐⭐ | ⚡ | Alta qualidade ⭐ |
| **large** | 1550MB | ⭐⭐⭐⭐⭐⭐ | ⚡ | Máxima precisão |

**Recomendação:** Use `medium` para melhor equilíbrio entre precisão e velocidade.

## 📝 Exemplo de Saída

### Com Timestamps (Padrão)
```
=== TRANSCRIÇÃO COM TIMESTAMPS ===

[0.00s - 3.50s] Olá, bem-vindo ao nosso podcast.
[3.50s - 8.20s] Hoje vamos falar sobre inteligência artificial.
[8.20s - 12.40s] É um tema muito interessante e atual.

=== TEXTO COMPLETO ===

Olá, bem-vindo ao nosso podcast. Hoje vamos falar sobre inteligência artificial. É um tema muito interessante e atual.
```

### Sem Timestamps
```
Olá, bem-vindo ao nosso podcast. Hoje vamos falar sobre inteligência artificial. É um tema muito interessante e atual.
```

## 🔧 Solução de Problemas

### "No module named transcriber"
```bash
# Certifique-se de definir o PYTHONPATH
$env:PYTHONPATH="src"; python -m transcriber audio.mp4
```

### CUDA não detectado
```bash
# Reinstale PyTorch com suporte CUDA
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Processamento muito lento
```bash
# Use modelo menor
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --model tiny

# Ou force CPU se GPU estiver ocupada
$env:PYTHONPATH="src"; python -m transcriber audio.mp4 --no-cuda
```

### FFmpeg não encontrado
```bash
# Windows (com chocolatey)
choco install ffmpeg

# Ou baixe em: https://ffmpeg.org/download.html
```

## 🏗️ Estrutura do Projeto

```
transcritor-audios/
├── src/
│   └── transcriber/
│       ├── __init__.py       # Exportações do módulo
│       ├── __main__.py       # Ponto de entrada
│       ├── cli.py            # Interface de linha de comando
│       ├── config.py         # Configurações
│       ├── extractor.py      # Extração de áudio de vídeos
│       ├── model.py          # Carregamento do modelo Whisper
│       └── transcribe.py     # Lógica principal de transcrição
├── install_dependencies.py  # Instalador de dependências
├── requirements.txt         # Dependências do projeto
├── .gitignore               # Arquivos ignorados pelo Git
├── LICENSE                  # Licença MIT
└── README.md                # Este arquivo
```

## 🎯 Exemplos de Uso

### Transcrever um podcast
```bash
$env:PYTHONPATH="src"; python -m transcriber podcast.mp3 --model medium --output podcast_texto.txt
```

### Transcrever vídeo do YouTube (após download)
```bash
$env:PYTHONPATH="src"; python -m transcriber video.mp4 --model medium --language pt
```

### Processar vários arquivos (PowerShell)
```powershell
Get-ChildItem *.mp4 | ForEach-Object {
    $env:PYTHONPATH="src"
    python -m transcriber $_.FullName --model medium
}
```

### Transcrição em inglês
```bash
$env:PYTHONPATH="src"; python -m transcriber audio_en.mp3 --language en --model medium
```

## 🚀 Performance

**Exemplo com arquivo de 10 minutos:**

| Modelo | GPU (RTX 4060) | CPU (i7) |
|--------|----------------|----------|
| tiny | ~15s | ~45s |
| base | ~20s | ~60s |
| small | ~30s | ~120s |
| medium | ~45s | ~180s |
| large | ~60s | ~300s |

*Tempos aproximados, variam conforme qualidade do áudio e hardware.*

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [OpenAI Whisper](https://github.com/openai/whisper) - Modelo de transcrição de áudio
- [PyTorch](https://pytorch.org/) - Framework de deep learning
- [FFmpeg](https://ffmpeg.org/) - Processamento de áudio/vídeo

## 📧 Contato

Para dúvidas ou sugestões, abra uma [issue](https://github.com/seu-usuario/transcritor-audios/issues) no GitHub.

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!
