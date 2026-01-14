# 1- Calculadora Básica (+, -, *, /)
print("1- Calculadora Básica")
num1 = float(input("Digite o primeiro número: "))
operacao = input("Operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Erro: operação inválida!"

print(f"Resultado: {resultado}")

# 2- Verificação de Média da Turma (8 caracteres)
print("\n2- Verificação de Média da Turma")
media_digitada = input("Digite a média da turma (8 caracteres): ")

if len(media_digitada) == 8:
    print("Válido: contém exatamente 8 caracteres")
else:
    print("Inválido: deve conter exatamente 8 caracteres")

# 3- Cálculo da Média da Turma
print("\n3- Cálculo da Média da Turma")
notas = []

for i in range(5):  # Exemplo com 5 alunos
    nota = float(input(f"Nota do aluno {i + 1}: "))
    notas.append(nota)

media_turma = sum(notas) / len(notas)
print(f"Média da turma: {media_turma:.2f}")

# 4- Classificação de Números Inseridos
print("\n4- Classificação de Números")
nums = []
quantos = int(input("Quantos números deseja inserir? "))

for i in range(quantos):
    n = float(input(f"Número {i + 1}: "))
    nums.append(n)

pares = sum(1 for n in nums if n % 2 == 0)
impares = len(nums) - pares

print("Números digitados:", nums)
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

print("\nCálculos concluídos.")

