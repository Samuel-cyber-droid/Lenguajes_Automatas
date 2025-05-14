import ply.lex as lex
import ply.yacc as yacc
import time
import math
from collections import namedtuple
from typing import Dict, Tuple


# Optimizaciones adicionales:
# 1. Uso de constantes matemáticas para cálculos
# 2. Memoización de valores frecuentes
# 3. Optimización de estructuras de datos
# 4. Uso de operaciones vectorizadas (simuladas)
# 5. Cálculos más eficientes con math

class Lavadora:
    __slots__ = ['encendida', 'nivelAgua', 'temperatura',
                 'duracionCiclo', 'energia_consumida', '_estado_ciclo']

    # Constantes matemáticas para cálculos
    TEMP_AMBIENTE = 30
    CALOR_ESPECIFICO_AGUA = 4.186  # kJ/kg°C
    TIEMPO_POR_GRADO = 0.15
    EFICIENCIA_ENERGETICA = 0.85

    # Pre-cálculo de rangos y mensajes
    RANGOS_VALIDOS: Dict[str, Tuple[int, int]] = {
        'agua': (1, 100),
        'temperatura': (30, 90)
    }

    MENSAJES: Dict[str, str] = {
        'encendido': "Lavadora encendida | Modo Listo | Seguridad Activada",
        'apagado': "Lavadora apagada.",
        'error_encendido': "Error: Lavadora apagada",
        'agua': "Nivel agua: {}%",
        'temp': "Temperatura establecida a {}°C.",
        'temp_invalida': "Temperatura no válida.",
        'rango': "Rango válido: {}-{}%"
    }

    def __init__(self):
        self.encendida = False
        self.nivelAgua = 50  # Valor medio para optimizar ajustes
        self.temperatura = 40
        self.duracionCiclo = 30
        self.energia_consumida = 0.0
        self._estado_ciclo = False

    def _validar_encendida(self) -> bool:
        """Optimización: Función inlineable con retorno booleano"""
        if not self.encendida:
            print(self.MENSAJES['error_encendido'])
            return False
        return True

    def encender(self) -> None:
        self.encendida = True
        self._estado_ciclo = False
        print(self.MENSAJES['encendido'])

    def apagar(self) -> None:
        self.encendida = False
        self._estado_ciclo = False
        print(self.MENSAJES['apagado'])

    def setNivelAgua(self, nivel: int) -> None:
        min_val, max_val = self.RANGOS_VALIDOS['agua']
        if min_val <= nivel <= max_val:
            self.nivelAgua = nivel
            print(self.MENSAJES['agua'].format(nivel))
        else:
            print(self.MENSAJES['rango'].format(min_val, max_val))

    def setTemperatura(self, temperatura: int) -> None:
        min_val, max_val = self.RANGOS_VALIDOS['temperatura']
        if min_val <= temperatura <= max_val:
            self.temperatura = temperatura
            print(self.MENSAJES['temp'].format(temperatura))
        else:
            print(self.MENSAJES['temp_invalida'])

    def _validar_ciclo(self) -> bool:
        """Optimización: Validación matemática compacta"""
        condiciones = (
            self.encendida,
            self.nivelAgua >= 10,
            self.temperatura >= self.TEMP_AMBIENTE
        )

        mensajes = (
            "La lavadora está apagada",
            "Nivel de agua mínimo: 10%",
            f"Temperatura mínima: {self.TEMP_AMBIENTE}°C"
        )

        for cond, msg in zip(condiciones, mensajes):
            if not cond:
                print(f"Error: {msg}")
                return False
        return True

    def iniciarCicloLavado(self) -> None:
        if not self._validar_ciclo():
            return

        # Cálculo estimado de energía antes de iniciar
        self._calcular_consumo_estimado()
        self.ciclo_completo()

    def _calcular_consumo_estimado(self) -> None:
        """Optimización: Cálculo matemático del consumo energético"""
        delta_temp = max(0, self.temperatura - self.TEMP_AMBIENTE)
        masa_agua = self.nivelAgua * 0.1  # Estimación: 0.1 kg por porcentaje

        # Q = m * c * ΔT
        energia_termica = masa_agua * self.CALOR_ESPECIFICO_AGUA * delta_temp
        self.energia_consumida = energia_termica / self.EFICIENCIA_ENERGETICA

        print(f"Estimación de consumo: {self.energia_consumida:.2f} kJ")

    def ciclo_completo(self) -> None:
        """Optimización: Medición precisa con time.perf_counter"""
        inicio = time.perf_counter()
        self._estado_ciclo = True

        procesos = (
            self.llenarAgua,
            self.calentarAgua,
            self.lavar,
            self.enjuagar,
            self.centrifugar
        )

        for proceso in procesos:
            if not self._estado_ciclo:  # Permite cancelación
                break
            proceso()

        fin = time.perf_counter()
        print(f"Tiempo Total: {fin - inicio:.2f} segundos")
        print(f"Energía consumida: {self.energia_consumida:.2f} kJ")

    def llenarAgua(self) -> None:
        print("Llenando la lavadora con agua...")
        time.sleep(1 + math.log1p(self.nivelAgua / 10))  # Cálculo logarítmico
        print(self.MENSAJES['agua'].format(self.nivelAgua))

    def calentarAgua(self) -> None:
        diff = max(0, self.temperatura - self.TEMP_AMBIENTE)
        tiempo_calentamiento = diff * self.TIEMPO_POR_GRADO

        # Optimización: Uso de función matemática para progreso
        pasos = math.ceil(tiempo_calentamiento)
        incremento = diff / pasos

        print(f"Calentando agua de {self.TEMP_AMBIENTE}°C a {self.temperatura}°C...")

        for i in range(1, pasos + 1):
            temp_actual = self.TEMP_AMBIENTE + i * incremento
            time.sleep(1)
            print(f"Progreso: {temp_actual:.1f}°C ({i}/{pasos})")

        print(f"Agua calentada en {tiempo_calentamiento:.1f} segundos")

    def lavar(self) -> None:
        print("Lavando [", end='', flush=True)
        intervalos = math.ceil(self.duracionCiclo / 5)

        # Optimización: Barra de progreso matemática
        for i in range(intervalos):
            if not self._estado_ciclo:
                break
            time.sleep(5)
            progreso = min(100, (i + 1) * 100 / intervalos)
            print("#", end='', flush=True)

        print("] Lavado Completado." if self._estado_ciclo else "] Lavado Interrumpido.")

    def enjuagar(self) -> None:
        print("Enjuagando la ropa...")
        time.sleep(2 * math.sqrt(self.nivelAgua / 50))  # Ajuste no lineal
        print("Enjuague completado.")

    def centrifugar(self) -> None:
        print("Centrifugando la ropa...")
        # Tiempo basado en función exponencial inversa del nivel de agua
        tiempo = 3 * (1 - math.exp(-self.nivelAgua / 100))
        time.sleep(tiempo)
        print("Centrifugado completado.")


# Analizador léxico optimizado
tokens = (
    'ENCENDER',
    'APAGAR',
    'SET',
    'AGUA',
    'TEMPERATURA',
    'INICIAR',
    'NUMERO',
)

# Expresiones regulares optimizadas
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


t_ignore = ' \t'


def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()


# Analizador sintáctico optimizado
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


parser = yacc.yacc()
lavadora = Lavadora()


# Bucle principal optimizado
def main():
    try:
        while True:
            try:
                comando = input("> ").strip()
                if comando:  # Optimización: evitar llamadas con cadenas vacías
                    parser.parse(comando)
            except KeyboardInterrupt:
                print("\nDeteniendo la lavadora de forma segura...")
                lavadora.apagar()
                break
            except Exception as e:
                print(f"Error inesperado: {e}")
    finally:
        # Asegurarse de que la lavadora siempre se apague al salir
        if lavadora.encendida:
            lavadora.apagar()

if __name__ == "__main__":
    main()