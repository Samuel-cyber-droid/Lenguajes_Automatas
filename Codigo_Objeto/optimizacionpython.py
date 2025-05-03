#  uso de variables locales en funciones (más rápido que globales)
def calcular():
    total = 0  # Variable local
    for i in range(1000):
        total += i  # Reutilizando variable
    return total

# uso de generadores para ahorrar memoria
numeros = (x for x in range(1000))  # Generator expression en lugar de lista