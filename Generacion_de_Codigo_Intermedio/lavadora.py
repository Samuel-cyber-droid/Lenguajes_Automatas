import ply.lex as lex
import ply.yacc as yacc
import time

class Lavadora:
    __slots__ = ('encendida', 'nivelAgua', 'temperatura', 'duracionCiclo')

    def __init__(self):
        self.encendida = False
        self.nivelAgua = 0
        self.temperatura = 30
        self.duracionCiclo = 2  # Más corto para pruebas

    def encender(self):
        self.encendida = True
        print("Lavadora encendida.")

    def apagar(self):
        self.encendida = False
        print("Lavadora apagada.")

    def setNivelAgua(self, nivel):
        if 1 <= nivel <= 100:
            self.nivelAgua = nivel
            print(f"Nivel de agua establecido a {nivel}%.")
        else:
            print("Nivel de agua no válido (1-100).")

    def setTemperatura(self, temperatura):
        if 30 <= temperatura <= 90:
            self.temperatura = temperatura
            print(f"Temperatura establecida a {temperatura}°C.")
        else:
            print("Temperatura no válida (30-90).")

    def iniciarCicloLavado(self):
        if not self.encendida:
            print("La lavadora está apagada. Enciéndela primero.")
            return

        print("Iniciando ciclo de lavado...")
        for paso in (self.llenarAgua, self.calentarAgua, self.lavar, self.enjuagar, self.centrifugar):
            paso()
        print("Ciclo de lavado completado.")

    def llenarAgua(self):
        print("Llenando agua...")
        time.sleep(1)
        print(f"Agua llena al {self.nivelAgua}%.")

    def calentarAgua(self):
        print(f"Calentando a {self.temperatura}°C...")
        time.sleep(1)
        print("Temperatura alcanzada.")

    def lavar(self):
        print("Lavando...")
        time.sleep(self.duracionCiclo)
        print("Lavado terminado.")

    def enjuagar(self):
        print("Enjuagando...")
        time.sleep(1)
        print("Enjuague listo.")

    def centrifugar(self):
        print("Centrifugando...")
        time.sleep(1)
        print("Centrifugado completo.")

# ---------- LEXER ----------
tokens = (
    'ENCENDER', 'APAGAR', 'SET', 'AGUA', 'TEMPERATURA', 'INICIAR', 'NUMERO',
)

t_ENCENDER = r'ENCENDER'
t_APAGAR = r'APAGAR'
t_SET = r'SET'
t_AGUA = r'AGUA'
t_TEMPERATURA = r'TEMPERATURA'
t_INICIAR = r'INICIAR'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caracter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# ---------- PARSER ----------
def p_comando_simple(p):
    '''comando : ENCENDER
               | APAGAR
               | INICIAR'''
    if p[1] == 'ENCENDER':
        lavadora.encender()
    elif p[1] == 'APAGAR':
        lavadora.apagar()
    elif p[1] == 'INICIAR':
        lavadora.iniciarCicloLavado()

def p_comando_param(p):
    '''comando : SET AGUA NUMERO
               | SET TEMPERATURA NUMERO'''
    if p[2] == 'AGUA':
        lavadora.setNivelAgua(p[3])
    elif p[2] == 'TEMPERATURA':
        lavadora.setTemperatura(p[3])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: entrada vacía o incompleta.")

parser = yacc.yacc()

# ---------- EJECUCIÓN PRINCIPAL ----------
if __name__ == "__main__":
    lavadora = Lavadora()
    print("Sistema de Lavadora. Escribe comandos como: ENCENDER, SET AGUA 50, INICIAR")
    try:
        while True:
            entrada = input("> ")
            if entrada.strip():
                parser.parse(entrada, lexer=lexer)
    except KeyboardInterrupt:
        print("\nSaliendo del sistema...")
