import csv

# Solicita ao usuário o nome do arquivo CSV
arquivo_csv = input("Digite o nome do arquivo CSV que deseja ler (ex: dados.csv): ")

try:
    # Abre o arquivo para leitura
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        leitor = csv.reader(file)
        
        # Lê cada linha do arquivo e imprime como lista
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print(f"Arquivo '{arquivo_csv}' não encontrado. Verifique o nome e tente novamente.")

except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
