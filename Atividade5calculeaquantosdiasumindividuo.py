from datetime import datetime

def calcular_dias_vividos(data_nascimento: str) -> int:
    """
    Calcula quantos dias uma pessoa está viva a partir da data de nascimento.
    
    Parâmetros:
    data_nascimento (str): Data de nascimento no formato 'DD/MM/AAAA'
    
    Retorna:
    int: Número de dias vividos
    """
    # Converte a string para objeto datetime
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    
    # Pega a data atual
    hoje = datetime.now()
    
    # Calcula a diferença em dias
    dias_vividos = (hoje - nascimento).days
    
    return dias_vividos

# --- Programa principal ---
data = input("Digite sua data de nascimento (DD/MM/AAAA): ")
try:
    dias = calcular_dias_vividos(data)
    print(f"Você está vivo há {dias} dias!")
except ValueError:
    print("Erro: digite a data no formato correto DD/MM/AAAA.")
