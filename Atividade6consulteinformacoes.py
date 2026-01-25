import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        # Verifica se o CEP existe
        if "erro" in dados:
            print("❌ CEP não encontrado.")
            return

        print("Endereço encontrado:")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro    : {dados.get('bairro', 'N/A')}")
        print(f"Cidade    : {dados.get('localidade', 'N/A')}")
        print(f"Estado    : {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException:
        print("❌ Falha na requisição. Verifique sua conexão.")

# Programa principal
cep_usuario = input("Digite o CEP (somente números): ").strip()
consultar_cep(cep_usuario)
