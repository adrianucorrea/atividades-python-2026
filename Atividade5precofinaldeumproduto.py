def calcular_preco_final(preco, porcentagem_desconto):
    """
    Calcula o preço final de um produto após aplicar um desconto percentual.
    
    Parâmetros:
    preco (float): Preço original do produto
    porcentagem_desconto (float): Porcentagem de desconto (ex: 10 para 10%)
    
    Retorna:
    float: Preço final arredondado para 2 casas decimais
    """
    valor_desconto = preco * (porcentagem_desconto / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)

# --- Programa principal ---
print("=== Calculadora de Preço com Desconto ===")

try:
    preco_produto = float(input("Digite o preço do produto: R$ ").replace(',', '.'))
    desconto = float(input("Digite a porcentagem de desconto: ").replace(',', '.'))

    preco_com_desconto = calcular_preco_final(preco_produto, desconto)
    print(f"Preço final após desconto: R$ {preco_com_desconto:.2f}")

except ValueError:
    print("Erro: Digite apenas números válidos para preço e desconto.")
