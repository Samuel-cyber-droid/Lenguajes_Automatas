def demostracion_optimizacion(n, base, exponente, a, r):
    print("\n--- DEMOSTRACION DE OPTIMIZACION MATEMATICA ---")

    #1. Suma de numeros consecutivos
    #bucle tradicional
    suma_bucle = 0
    for i in range(1, n+1):
        suma_bucle += i

    # forma matematica
    suma_math = n * (n + 1) // 2

    print(f"\n1. Suma de 1 a {n}:")
    print(f"Bucle: {suma_bucle} | Formula: {suma_math} | Iguales: {suma_bucle == suma_math}")

    #2. Suma de numeros pares
    suma_pares_bucle = 0
    for i in range(2, n+1, 2):
        suma_pares_bucle += i

    k = n // 2
    suma_pares_math = k * (k + 1)
    print(f"\n2. Suma de pares hastra {n}:")
    print(f"Bucle: {suma_pares_bucle} | Formula: {suma_pares_math} | Igual: {suma_pares_bucle == suma_pares_math}")

    #3.Calculo de Potencias
    potencia_bucle = 1
    for _ in range(exponente):
        potencia_bucle *= base

    potencia_math = base ** exponente

    print(f"\n3. Potnecia: {base}^{exponente}:")
    print(f"Bucle: {potencia_bucle} | Formula: {potencia_math} | Iguales {potencia_bucle == potencia_math}")

    #4. Suma de serie geometrica
    serie_bucle = 0
    for i in range(n):
        serie_bucle += a * (r ** i)

    if r != 1:
        serie_math = a * (1 - r ** n) / (1 -r)
    else:
        serie_math = a * n

    print(f"\n4. Serie geométrica (a={a}, r={r}, términos={n}):")
    print(f"Bucle: {serie_bucle} | Fórmula: {serie_math} | Iguales: {round(serie_bucle, 6) == round(serie_math, 6)}")

# ejecutar demostracion
demostracion_optimizacion(n = 100, base = 2, exponente = 10, a = 1, r = 0.5)