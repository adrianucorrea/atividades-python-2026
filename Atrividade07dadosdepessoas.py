import csv

# Lista de listas com dados fictícios de pessoas
pessoas = [
    ["João Silva", 28, "São Paulo"],
    ["Maria Oliveira", 35, "Rio de Janeiro"],
    ["Carlos Souza", 22, "Belo Horizonte"]
]

# Solicita ao usuário o nome do arquivo CSV
arquivo_csv = input("Digite o nome do arquivo CSV para salvar os dados (ex: dados.csv): ")

try:
    # Abre o arquivo para escrita
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        
        # Escreve o cabeçalho
        escritor.writerow(["Nome", "Idade", "Cidade"])
        
        # Escreve os dados das pessoas linha por linha
        for pessoa in pessoas:
            escritor.writerow(pessoa)
    
    print(f"Dados gravados com sucesso no arquivo '{arquivo_csv}'!")

except Exception as e:
    print(f"Ocorreu um erro ao escrever o arquivo: {e}")
