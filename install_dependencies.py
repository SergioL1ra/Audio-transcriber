"""
Instalador automático de dependências para o Transcritor de Áudio
"""

import subprocess
import sys

def install_pytorch_cuda():
    """Instala PyTorch com suporte CUDA."""
    print("🔧 Instalando PyTorch com suporte CUDA...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "torch", "torchaudio",
            "--index-url", "https://download.pytorch.org/whl/cu118"
        ])
        print("✅ PyTorch com CUDA instalado com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("⚠️  Erro ao instalar PyTorch com CUDA. Tentando versão CPU...")
        return False

def install_basic_requirements():
    """Instala dependências básicas do requirements.txt."""
    print("\n🔧 Instalando dependências básicas...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependências básicas instaladas!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def check_cuda():
    """Verifica se CUDA está disponível."""
    try:
        import torch
        if torch.cuda.is_available():
            print(f"\n✅ CUDA detectado: {torch.cuda.get_device_name(0)}")
            return True
        else:
            print("\n⚠️  CUDA não detectado. Executará em CPU.")
            return False
    except ImportError:
        return False

def main():
    print("=" * 60)
    print("INSTALADOR DE DEPENDÊNCIAS - TRANSCRITOR DE ÁUDIO")
    print("=" * 60)
    
    # Instala PyTorch com CUDA
    cuda_success = install_pytorch_cuda()
    
    if not cuda_success:
        # Fallback para requirements.txt padrão
        install_basic_requirements()
    
    # Verifica instalação
    print("\n🔍 Verificando instalação...")
    check_cuda()
    
    print("\n✅ Instalação concluída!")
    print("\n📖 Uso:")
    print("  $env:PYTHONPATH=\"src\"; python -m transcriber audio.mp4")
    print("  $env:PYTHONPATH=\"src\"; python -m transcriber audio.mp4 --model medium")

if __name__ == "__main__":
    main()
