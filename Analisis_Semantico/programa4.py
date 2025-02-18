import ply.lex as lex
from difflib import SequenceMatcher

# Definir los tokens
tokens = (
    'NUMERO',
)

# Definir reglas para los tokens
t_NUMERO = r'\+?[0-9\s]{7,15}'

# Ignorar espacios
t_ignore = ' \t'

# Manejar errores
def t_error(t):
    print(f"Error de análisis: {t.value[0]}")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

def jaccard_index(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Ejemplo de uso
def main():
    telefono1 = input("Introduce el primer número de teléfono: ")
    telefono2 = input("Introduce el segundo número de teléfono: ")

    # Analizar los números
    lexer.input(telefono1)
    if not any(token.type == 'NUMERO' for token in lexer):
        print("El primer número de teléfono no es válido.")
        return

    lexer.input(telefono2)
    if not any(token.type == 'NUMERO' for token in lexer):
        print("El segundo número de teléfono no es válido.")
        return

    print("Ambos números de teléfono son válidos.")
    indice_jaccard = jaccard_index(telefono1, telefono2)
    print(f"Índice de Jaccard: {indice_jaccard:.2f}")

if _name_ == "_main_":
    main()
