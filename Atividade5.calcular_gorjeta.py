def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# --- Programa principal ---
valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
total = valor + valor_gorjeta

print(f"Gorjeta a ser deixada: R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
