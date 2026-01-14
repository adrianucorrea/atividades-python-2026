# 1- Conversor de Moeda
print("1- Conversor de Moeda")
valor_reais = float(input("Valor em reais (R$): "))
taxa_dolar = float(input("Taxa do dólar (R$/USD): "))

valor_dolar = valor_reais / taxa_dolar
print(f"Valor em USD: US$ {valor_dolar:.2f}")

# 2- Calculadora de Desconto
print("\n2- Calculadora de Desconto")
preco_original = float(input("Preço original (R$): "))
percentual = float(input("Percentual de desconto (%): "))

desconto = (preco_original * percentual) / 100
preco_final = preco_original - desconto

print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# 3- Calculadora de Média Escolar
print("\n3- Calculadora de Média Escolar")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3
resultado = "Aprovado" if media >= 7 else "Reprovado"

print(f"Média: {media:.1f} - {resultado}")

# 4- Calculadora de Consumo de Combustível
print("\n4- Calculadora de Consumo de Combustível")
km_percorrido = float(input("Km percorridos: "))
litros = float(input("Litros consumidos: "))

consumo = km_percorrido / litros
print(f"Consumo médio: {consumo:.2f} Km/L")

print("\nCálculos concluídos.")
