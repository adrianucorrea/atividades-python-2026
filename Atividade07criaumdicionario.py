import json
import os

def criar_e_salvar_json():
    # 1. Criar o dicionário com dados de uma pessoa
    dados_pessoa = {
        "nome": "João Silva",
        "idade": 30,
        "cidade": "São Paulo",
        "profissao": "Engenheiro de Software"
    }

    print("--- Gerenciador de Dados JSON ---")
    print(f"Dados a serem salvos: {dados_pessoa}")

    # 2. Solicitar o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.json): ").strip()
    
    # Garantir que tenha a extensão .json
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    try:
        # 3. Salvar os dados no arquivo usando json.dump()
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_pessoa, arquivo, indent=4, ensure_ascii=False)
        print(f"\n[Sucesso] Dados salvos com sucesso em '{nome_arquivo}'.")

        # 4. Ler o mesmo arquivo e imprimir os dados carregados usando json.load()
        print("\nLendo dados do arquivo...")
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados_carregados = json.load(arquivo)
                print("Conteúdo carregado:")
                for chave, valor in dados_carregados.items():
                    print(f" - {chave.capitalize()}: {valor}")
        else:
            print("[Erro] O arquivo não foi encontrado após a escrita.")

    except IOError as e:
        print(f"[Erro] Ocorreu um erro de entrada/saída: {e}")
    except json.JSONDecodeError:
        print("[Erro] Falha ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"[Erro] Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    criar_e_salvar_json()