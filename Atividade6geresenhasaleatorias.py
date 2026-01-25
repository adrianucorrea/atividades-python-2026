import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres
    letras = string.ascii_letters      # a-z e A-Z
    numeros = string.digits            # 0-9
    simbolos = string.punctuation      # !@#$%...

    # Junta tudo
    caracteres = letras + numeros + simbolos

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
try:
    tamanho = int(input("Digite o tamanho da senha: "))

    if tamanho < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")

except ValueError:
    print("Por favor, digite um número válido.")
