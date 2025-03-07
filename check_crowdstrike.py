import os
import winreg
import subprocess

# Caminho onde o CrowdStrike geralmente fica instalado
cs_path = r"C:\Program Files\CrowdStrike"
temp_file = r"C:\Windows\Temp\CrowdStrike_Installed.txt"

def is_crowdstrike_installed():
    """Verifica se o CrowdStrike Falcon está instalado no sistema."""
    
    # Verifica se a pasta do programa existe
    if os.path.exists(cs_path):
        return True

    # Verifica no registro do Windows
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\CSFalconService") as key:
            return True
    except FileNotFoundError:
        pass

    # Verifica se o serviço CSFalconService está rodando
    try:
        result = subprocess.run(["sc", "query", "CSFalconService"], capture_output=True, text=True)
        if "RUNNING" in result.stdout or "STOPPED" in result.stdout:
            return True
    except Exception:
        pass

    return False

def create_temp_file():
    """Cria um arquivo indicando que o CrowdStrike está instalado."""
    with open(temp_file, "w") as f:
        f.write("CrowdStrike Falcon esta instalado neste sistema.")

def main():
    if is_crowdstrike_installed():
        create_temp_file()
        print(f"✅ CrowdStrike encontrado! Arquivo criado em {temp_file}")
    else:
        print("❌ CrowdStrike não encontrado. Nenhum arquivo foi criado.")

if __name__ == "__main__":
    main()
