# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:51:08 2025

@author: samy2
"""

import ply.lex as lex
import ply.yacc as yacc
import sys

# Definición de tokens
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE']

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Expresión regular para reconocer números enteros
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

# Reglas de precedencia y asociatividad
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Reglas de la gramática
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = ('-', p[1], p[3])

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = ('*', p[1], p[3])

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = ('/', p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p is None:
        print("Error de sintaxis: entrada inesérada")
    else:
        print("Error de sintaxis en '%s'" % p.value)
    sys.exit(1)

# Construcción del parser
parser = yacc.yacc()

# Función para evaluar el AST
def evaluate_expression(ast):
    if isinstance(ast, tuple):
        operator, left, right = ast
        if operator == '+':
            return evaluate_expression(left) + evaluate_expression(right)
        elif operator == '-':
            return evaluate_expression(left) - evaluate_expression(right)
        elif operator == '*':
            return evaluate_expression(left) * evaluate_expression(right)
        elif operator == '/':
            return evaluate_expression(left) / evaluate_expression(right)
    else:
        return ast

# Ejemplo de uso
data = "3 + 5 * 2"
lexer.input(data)

# Obtener los tokens reconocidos
while True:
    token = lexer.token()
    if not token:
        break
    print(token)

# Parsear la expresión
result = parser.parse(data)
print("AST:", result)

# Evaluar la expresión
evaluated_result = evaluate_expression(result)
print("Resultado de la evaluación:", evaluated_result)