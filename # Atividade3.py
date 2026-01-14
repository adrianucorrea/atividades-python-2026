# 1- Classificador de Idade
print("1- Classificador de Idade")
idade = int(input("Digite sua idade (anos): "))

if 0 <= idade < 13:
    print("Criança (0–12 anos)")
elif 13 <= idade < 18:
    print("Adolescente (13–17 anos)")
elif 18 <= idade < 60:
    print("Adulto (18–59 anos)")
else:
    print("Idoso (60+ anos)")

# 2- Calculadora de IMC
print("\n2- Calculadora de IMC")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Acima do peso")

# 3- Conversor de Temperatura
print("\n3- Conversor de Temperatura")
celsius = float(input("Temperatura em Celsius (°C): "))

fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

# 4- Verificador de Ano Bissexto
print("\n4- Verificador de Ano Bissexto")
ano = int(input("Digite um ano: "))

bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
print("Ano bissexto" if bissexto else "Ano não bissexto")

print("\nCálculos concluídos.")

