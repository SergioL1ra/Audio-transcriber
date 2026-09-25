"""
Instalador automático de dependências para o Transcritor de Áudio (faster-whisper)
"""

import subprocess
import sys

def configure_encoding():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

def install_pytorch_cuda():
    """Instala PyTorch com suporte a CUDA 12.1."""
    print("🔧 Instalando PyTorch com suporte a CUDA 12.1...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "torch", "torchaudio",
            "--index-url", "https://download.pytorch.org/whl/cu121",
            "--no-cache-dir"
        ])
        print("✅ PyTorch com CUDA 12.1 instalado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar PyTorch com CUDA: {e}")
        return False

def install_requirements():
    """Instala dependências do requirements.txt sem sobrescrever PyTorch."""
    print("\n🔧 Instalando faster-whisper e moviepy...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependências instaladas!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def check_cuda():
    """Verifica se CUDA está disponível."""
    try:
        import torch
        print(f"\n🔍 Versão do PyTorch: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"✅ CUDA detectado e ATIVO! Dispositivo: {torch.cuda.get_device_name(0)}")
            return True
        else:
            print("⚠️ CUDA não detectado pelo PyTorch. Executará em modo CPU.")
            return False
    except ImportError:
        print("❌ PyTorch não foi instalado corretamente.")
        return False

def main():
    configure_encoding()
    print("=" * 60)
    print("INSTALADOR DE DEPENDÊNCIAS - TRANSCRITOR DE ÁUDIO (faster-whisper)")
    print("=" * 60)
    
    install_pytorch_cuda()
    install_requirements()
    
    print("\n🔍 Verificando instalação de hardware...")
    check_cuda()
    
    print("\n✅ Instalação concluída!")
    print("\n📖 Uso (com venv ativado):")
    print("  .\\venv\\Scripts\\python.exe -m transcriber audio.mp4")
    print("  .\\venv\\Scripts\\python.exe -m transcriber audio.mp4 --model medium")

if __name__ == "__main__":
    main()
