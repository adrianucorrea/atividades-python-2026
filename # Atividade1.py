# Programa 1: Saudação e Soma
print("Olá, mundo!")
print("Crie um programa que imprima uma mensagem 'Olá, mundo!' na tela.")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2
print(f"Soma: {soma}")

# Programa 2: Volume de uma caixa retangular
print("3- Crie um programa de cálculo de volume de uma caixa retangular.")
comprimento = float(input("Comprimento (cm): "))
largura = float(input("Largura (cm): "))
altura = float(input("Altura (cm): "))
volume = comprimento * largura * altura
print(f"Volume = {volume} cm³")

# Programa 3: Preço total de um produto
print("4- Crie um programa de cálculo do preço total e exibir todas as informações")
preco_unit = float(input("Preço unitário (R$): "))
quantidade = int(input("Quantidade: "))
total = preco_unit * quantidade

# Programa 4: Exibição consolidada
print("Programa 4 Resumo Geral")
print("- Programa 1 - Soma:", soma)
print("- Programa 2 - Volume:", volume, "cm³")
print("- Programa 3 - Informações")
print(f"  Preço unitário R$ {preco_unit}")
print(f"  Quantidade {quantidade}")
print(f"  Preço total R$ {total:.2f}")
print("Todos os cálculos concluídos.")
