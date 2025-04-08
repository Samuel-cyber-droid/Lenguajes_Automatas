import ply.lex as lex
import ply.yacc as yacc
import time

# Optimizaciones Globales (mejoras en toda la clase)
# Optimizacion de Memoria (Global)
# Clase de la lavadora
class Lavadora:
    __slots__ = ['encendida', 'nivelAgua', 'temperatura',
                 'duracionCiclo', 'energia_consumida']

    def __init__(self):
        # Estado inicial optimizado (valores por defecto)
        self.encendida = False
        self.nivelAgua = 50 # Valor por defecto más práctico
        self.temperatura = 40
        self.duracionCiclo = 30
        self.energia_consumida = 0

    # Metodo unificado para validaciones
    def _validar_encendida(self):
        if not self.encendida:
            print("Error: Lavadora apagada")
            return False
        return True

    #Optimizacion de Codigo Muerto (Mirilla)
    MENSAJES = {
        'encendido': "Lavadora encendida | Modo Listo | Seguridad Activada"
    }
    def encender(self):
        self.encendida = True
        print(self.MENSAJES['encendido'])

    def apagar(self):
        self.encendida = False
        print("Lavadora apagada.")

    #Optimizacion de Mirilla (peephole - pequeñas optimizaciones puntuales)
    # optimizado: precalcular rangos y mensajes
    RANGOS_VALIDOS = {
        'agua': (1, 100),
        'temperatura': (30, 90)
    }

    def setNivelAgua(self, nivel):
        min_val, max_val = self.RANGOS_VALIDOS['agua']
        if min_val <= nivel <= max_val:
            self.nivelAgua = nivel
            print(f"Nivel agua: {nivel}%" )
        else:
            print(f"Rango valido: {min_val}-{max_val}%")

    def setTemperatura(self, temperatura):
        if 30 <= temperatura <= 90:
            self.temperatura = temperatura
            print(f"Temperatura establecida a {temperatura}°C.")
        else:
            print("Temperatura no válida.")

    # Optimizacion Combinada (Ciclos  + Mirilla)
    # Optimizado: Validacion unificada
    def _validar_ciclo(self):
        checks = [
            (self.encendida, "La lavadora esta apagada"),
            (self.nivelAgua >= 10, "Nivel de agua minimo: 10%"),
            (self.temperatura >= 30, "Temperatura minima: 30°C")
        ]
        for condicion, mensaje in checks:
            if not condicion:
                print(f"Error: {mensaje}")
                return False
        return True

    #  Optimizado: validacion unificada y tiempo total acumulado
    def iniciarCicloLavado(self):
        if not self._validar_ciclo():
            return
        self.ciclo_completo()

    def ciclo_completo(self):
        inicio = time.time()
        self.llenarAgua()
        self.calentarAgua()
        self.lavar()
        self.enjuagar()
        self.centrifugar()
        fin = time.time()
        print(f"Tiempo Total: {fin - inicio:.2f} segundos")

    def llenarAgua(self):
        print("Llenando la lavadora con agua...")
        time.sleep(2)
        print(f"Lavadora llena al {self.nivelAgua}%.")

    # Optimizacion Local (dentro de metodos/funciones especificas)
    # Optimizado (Cáñculo dinámico del tiempo basado en diferencia térmica)
    def calentarAgua(self):
        temp_inicial = 30 # temperatura ambiente base
        diff = max(0, self.temperatura - temp_inicial)
        tiempo_calentamineto = round(diff * 0.15, 1) # .15 seg por grado
        print(f"Calentando agua de {temp_inicial}°C a {self.temperatura}°C....")
        time.sleep(tiempo_calentamineto)
        print(f"Agua calentada: {tiempo_calentamineto} segundos")

    # Optimizaciones de Ciclos (mejora en bucles y procesos repetitivos)
    # Optimizado: Proceso en tiempo real con intervalos
    def lavar(self):
        print("Lavando [", end='', flush=True)
        intervalos = self.duracionCiclo // 5 # Actualizacion cada 5 seg
        for _ in range(intervalos):
            time.sleep(5)
            print("#", end='', flush=True)
        print("] Lavado Completado.")

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
    print("Iniciando ciclo de lavado....")
    lavadora.iniciarCicloLavado()

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: comando incompleto")

# Crear el parser
parser = yacc.yacc()

# Instancia de la lavadora
lavadora = Lavadora()

# Bucle principal
while True:
    try:
        comando = input("> ").strip()
        if not comando:
            continue
        parser.parse(comando)
    except EOFError:
        break