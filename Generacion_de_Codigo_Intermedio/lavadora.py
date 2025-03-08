import ply.lex as lex
import ply.yacc as yacc
import time

# Clase de la lavadora
class Lavadora:
    def __init__(self):
        self.encendida = False
        self.nivelAgua = 0
        self.temperatura = 30
        self.duracionCiclo = 30

    def encender(self):
        self.encendida = True
        print("Lavadora encendida.")

    def apagar(self):
        self.encendida = False
        print("Lavadora apagada.")

    def setNivelAgua(self, nivel):
        if 0 <= nivel <= 100:
            self.nivelAgua = nivel
            print(f"Nivel de agua establecido a {nivel}%.")
        else:
            print("Nivel de agua no válido.")

    def setTemperatura(self, temperatura):
        if 30 <= temperatura <= 90:
            self.temperatura = temperatura
            print(f"Temperatura establecida a {temperatura}°C.")
        else:
            print("Temperatura no válida.")

    def iniciarCicloLavado(self):
        if not self.encendida:
            print("La lavadora está apagada. Enciéndela primero.")
            return

        print("Iniciando ciclo de lavado...")
        self.llenarAgua()
        self.calentarAgua()
        self.lavar()
        self.enjuagar()
        self.centrifugar()
        print("Ciclo de lavado completado.")

    def llenarAgua(self):
        print("Llenando la lavadora con agua...")
        time.sleep(2)
        print(f"Lavadora llena al {self.nivelAgua}%.")

    def calentarAgua(self):
        print(f"Calentando el agua a {self.temperatura}°C...")
        time.sleep(3)
        print(f"Agua calentada a {self.temperatura}°C.")

    def lavar(self):
        print("Lavando la ropa...")
        time.sleep(self.duracionCiclo)
        print("Lavado completado.")

    def enjuagar(self):
        print("Enjuagando la ropa...")
        time.sleep(2)
        print("Enjuague completado.")

    def centrifugar(self):
        print("Centrifugando la ropa...")
        time.sleep(2)
        print("Centrifugado completado.")


# Analizador léxico
tokens = (
    'ENCENDER',
    'APAGAR',
    'SET',
    'AGUA',
    'TEMPERATURA',
    'INICIAR',
    'NUMERO',
)

# Expresiones regulares para tokens
t_ENCENDER = r'ENCENDER'
t_APAGAR = r'APAGAR'
t_SET = r'SET'
t_AGUA = r'AGUA'
t_TEMPERATURA = r'TEMPERATURA'
t_INICIAR = r'INICIAR'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

# Analizador sintáctico
def p_comando_encender(p):
    'comando : ENCENDER'
    lavadora.encender()

def p_comando_apagar(p):
    'comando : APAGAR'
    lavadora.apagar()

def p_comando_set_agua(p):
    'comando : SET AGUA NUMERO'
    lavadora.setNivelAgua(p[3])

def p_comando_set_temperatura(p):
    'comando : SET TEMPERATURA NUMERO'
    lavadora.setTemperatura(p[3])

def p_comando_iniciar(p):
    'comando : INICIAR'
    lavadora.iniciarCicloLavado()

def p_error(p):
    print("Error de sintaxis.")

# Crear el parser
parser = yacc.yacc()

# Instancia de la lavadora
lavadora = Lavadora()

# Bucle principal
while True:
    try:
        comando = input("> ")
        parser.parse(comando)
    except EOFError:
        break