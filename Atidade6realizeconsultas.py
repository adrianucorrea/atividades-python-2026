import requests
from datetime import datetime

def consultar_moeda(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("❌ Moeda não encontrada.")
            return

        info = dados[chave]

        valor_atual = info["bid"]
        maxima = info["high"]
        minima = info["low"]
        timestamp = int(info["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nCotação {moeda} → BRL")
        print(f"Valor atual : R$ {valor_atual}")
        print(f"Máxima      : R$ {maxima}")
        print(f"Mínima      : R$ {minima}")
        print(f"Atualizado  : {data_hora}")

    except requests.exceptions.RequestException:
        print("❌ Erro na requisição. Verifique sua conexão ou tente mais tarde.")

# Programa principal
moeda_usuario = input("Digite a moeda (ex: USD, EUR, BTC): ")
consultar_moeda(moeda_usuario)
