import unicodedata

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é palíndromo, ignorando espaços, pontuação e acentos.
    
    Parâmetros:
    texto (str): Palavra ou frase a ser verificada
    
    Retorna:
    str: "Sim" se for palíndromo, "Não" caso contrário
    """
    # Normaliza para remover acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(char for char in texto if unicodedata.category(char) != 'Mn')
    
    # Remove espaços e pontuação, deixa tudo em minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    
    # Verifica se é igual ao inverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# --- Teste da função ---
frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"Palíndromo? {resultado}")
