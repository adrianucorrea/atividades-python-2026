# 1- Calculadora básica (+, -, *, /)
print("1- Criar código que usa calculadora tenha operações básicas (+, -, *, /)")
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
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"
print(f"Resultado: {resultado}")

# 2- Verificar se é média da turma (8 caracteres)
print("\n2- Criar código que verifica se é média turma")
media_digitada = input("Digite a média da turma (8 caracteres): ")
if len(media_digitada) == 8:
    print("Válido: 8 caracteres")
else:
    print("Inválido: deve ter exatamente 8 caracteres")

# 3- Calcular média turma
print("\n3- Criar código para verificar cálculo média turma")
notas = []
for i in range(5):  # 5 alunos exemplo
    nota = float(input(f"Nota aluno {i+1}: "))
    notas.append(nota)
media_turma = sum(notas) / len(notas)
print(f"Média turma: {media_turma:.2f}")

# 4- Classificar números inseridos
print("\n4- Criar código que seja para analisar números digitados pelo usuário")
nums = []
quantos = int(input("Quantos números inserir? "))
for i in range(quantos):
    n = float(input(f"Número {i+1}: "))
    nums.append(n)
print("Números:", nums)
pares = sum(1 for n in nums if n % 2 == 0)
print(f"Pares: {pares}, Ímpares: {len(nums)-pares}")
