# Importar librerías
import ply.lex as lex
import ply.yacc as yacc
import sys

# Definición de tokens
tokens = ['NUMBER']

# Definición de expresión regular para números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar caracteres como espacios y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores de token
def t_error(t):
    print("Caracter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Regla de la gramática para una expresión que es un número
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Manejo de errores de sintaxis
def p_error(p):
    if p is None:
        print("Error de sintaxis: entrada inesperada")
    else:
        print("Error de sintaxis en '%s'" % p.value)
    sys.exit(1)

# Construcción del parser
parser = yacc.yacc()

# Ejemplo de uso
data = "6"
lexer.input(data)

# Obtener los tokens reconocidos
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Parsear la expresión
result = parser.parse(data)
if result is not None:  # Si el parser devuelve un valor, es un número entero válido
    print("El número es entero")
else:
    print("Error: La entrada no es un número entero válido")
    sys.exit(1)