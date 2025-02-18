import ply.lex as lex

# Definición de los tokens
tokens = (
    'USER',
    'AT',
    'DOMAIN',
    'TLD',
)

# Definición de los tokens y sus expresiones regulares
t_USER = r'[a-zA-Z0-9._%+-]+'
t_AT = r'@'
t_DOMAIN = r'[a-zA-Z0-9.-]+'
t_TLD = r'\.[a-zA-Z]{2,}'

# Ignorar espacios
t_ignore = ' \t\n'

# Manejar errores
def t_error(t):
    print(f"Error de análisis: '{t.value}' no es un token válido")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

def validar_correo(correo):
    lexer.input(correo)
    tokens_encontrados = [tok.type for tok in lexer]
    
    # Verificar si se encontraron todos los tokens necesarios
    return tokens_encontrados == ['USER', 'AT', 'DOMAIN', 'TLD']

def calcular_jaccard(correo1, correo2):
    # Convertir los correos a conjuntos de caracteres
    set1 = set(correo1)
    set2 = set(correo2)
    
    # Calcular el índice de Jaccard
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union if union != 0 else 0

def main():
    correo = input("Ingrese una dirección de correo electrónico: ")

    if validar_correo(correo):
        print("La dirección de correo electrónico es válida.")
    else:
        print("La dirección de correo electrónico no es válida.")

    # Ejemplo de uso de Jaccard para comparar dos correos
    correo_comparar = input("Ingrese un segundo correo para comparar: ")
    index = calcular_jaccard(correo, correo_comparar)
    print(f"Índice de Jaccard entre los correos: {index:.2f}")

if __name__ == "__main__":
    main()
