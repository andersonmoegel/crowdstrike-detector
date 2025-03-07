# Documentação do Script de Verificação e Registro do CrowdStrike Falcon

Este script verifica se o **CrowdStrike Falcon** está instalado no sistema e cria um arquivo temporário em caso afirmativo, indicando que o programa está presente. Ele realiza a verificação utilizando três métodos diferentes: pasta de instalação, chave de registro e serviço em execução.

## Funcionalidades

1. **Verificação da instalação do CrowdStrike Falcon**:
   - Verifica se a pasta onde o CrowdStrike geralmente é instalado existe.
   - Verifica se a chave de registro referente ao serviço do CrowdStrike está presente.
   - Verifica se o serviço `CSFalconService` está em execução.

2. **Criação de um arquivo temporário**:
   - Caso o CrowdStrike seja encontrado, um arquivo temporário é criado para registrar essa informação.

3. **Exibição de mensagem**:
   - O script exibe no terminal se o CrowdStrike foi encontrado e se o arquivo foi criado com sucesso.

## Estrutura do Código

### 1. Importação de Bibliotecas

```python
import os
import winreg
import subprocess
```

Essas bibliotecas são usadas para verificar a existência do CrowdStrike e manipular o sistema:
- **`os`**: Para manipulação de caminhos e verificação da existência de pastas.
- **`winreg`**: Para acessar o registro do Windows e verificar se a chave do serviço do CrowdStrike está presente.
- **`subprocess`**: Para executar comandos do sistema, como a verificação do status do serviço `CSFalconService`.

### 2. Variáveis de Configuração

#### Caminho do CrowdStrike e Arquivo Temporário

```python
cs_path = r"C:\Program Files\CrowdStrike"
temp_file = r"C:\Windows\Temp\CrowdStrike_Installed.txt"
```

- **`cs_path`**: Caminho onde o CrowdStrike Falcon geralmente está instalado no sistema.
- **`temp_file`**: Caminho onde será criado o arquivo temporário caso o CrowdStrike seja encontrado.

### 3. Funções

#### `is_crowdstrike_installed()`

```python
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
```

Esta função realiza três verificações para determinar se o **CrowdStrike Falcon** está instalado:
1. Verifica se a pasta de instalação (`C:\Program Files\CrowdStrike`) existe.
2. Tenta acessar o registro do Windows, procurando pela chave `CSFalconService` que indica a instalação do CrowdStrike.
3. Verifica se o serviço `CSFalconService` está em execução usando o comando `sc query`.

Se qualquer uma dessas verificações for bem-sucedida, a função retorna `True`, indicando que o CrowdStrike está instalado. Caso contrário, retorna `False`.

#### `create_temp_file()`

```python
def create_temp_file():
    """Cria um arquivo indicando que o CrowdStrike está instalado."""
    with open(temp_file, "w") as f:
        f.write("CrowdStrike Falcon esta instalado neste sistema.")
```

Esta função cria um arquivo temporário no caminho `C:\Windows\Temp\CrowdStrike_Installed.txt`, contendo a mensagem `"CrowdStrike Falcon esta instalado neste sistema."`.

#### `main()`

```python
def main():
    if is_crowdstrike_installed():
        create_temp_file()
        print(f"✅ CrowdStrike encontrado! Arquivo criado em {temp_file}")
    else:
        print("❌ CrowdStrike não encontrado. Nenhum arquivo foi criado.")
```

A função `main()` é responsável por orquestrar o processo:
1. Verifica se o CrowdStrike está instalado usando a função `is_crowdstrike_installed()`.
2. Se o CrowdStrike for encontrado, chama a função `create_temp_file()` para criar o arquivo temporário e imprime uma mensagem de sucesso.
3. Caso o CrowdStrike não seja encontrado, imprime uma mensagem de erro.

### 4. Execução do Script

```python
if __name__ == "__main__":
    main()
```

Essa linha garante que o script será executado apenas quando for chamado diretamente, não quando for importado como módulo. A função `main()` é chamada para iniciar o processo.

## Uso

1. **Executar o script**: Para rodar o script, basta executá-lo em um ambiente Python. Ele verificará se o **CrowdStrike Falcon** está instalado no sistema e criará um arquivo indicando isso.
2. **Verificar o arquivo de resultado**: Após a execução, o arquivo `CrowdStrike_Installed.txt` será criado em `C:\Windows\Temp\` se o CrowdStrike for encontrado.

## Possíveis Melhorias

- **Aprimoramento na gestão de erros**: O script pode ser melhorado para registrar erros mais detalhados no caso de falha nas verificações (por exemplo, ao tentar acessar o registro ou verificar o serviço).
- **Suporte a múltiplas versões do CrowdStrike**: A verificação pode ser aprimorada para lidar com diferentes versões do CrowdStrike, caso seja necessário.

## Conclusão

Este script fornece uma maneira simples e eficaz de verificar a instalação do **CrowdStrike Falcon** no sistema, utilizando múltiplos métodos de verificação, e cria um arquivo temporário como confirmação. Ele é útil para administradores de sistemas e usuários que desejam confirmar a presença do software de segurança.
