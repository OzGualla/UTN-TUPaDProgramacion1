
""" Tp10 - Recursividad """

# ========================
# Declaración de variables
# ========================

import sys
sys.setrecursionlimit(2000)

# Validación de entradas
def validar_numero(mensaje):
    """
    Pide input str()
    Retorna int(validado)
    """
    while True:
        num = input(mensaje)
        if not num.isdigit():
            print("Solo se aceptan números positivos")
            continue

        num = int(num)
        if num <= 0:
            print("Error: El número no puede ser igual o menor a 0")
            continue

        return num
    
# ============
# Ejercicio 1:
# ============

def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)

# ============
# Ejercicio 2:
# ============

def fibonacci_recursivo(num):
    # Casos base
    if num == 0:
        return 0
    elif num == 1:
        return 1
    # En cada iteración F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)
    
def ver_serie_fibonacci(num):
    """
    Recibe el numero ingresado
    Recorre y muestra la serie por posición
    """
    print(f"\nSerie de Fibonacci hasta la posición {num}\n")
    for i in range(num + 1):
        valor = fibonacci_recursivo(i)
        print(f"Posición: {i} = {valor}")

# ============
# Ejercicio 3:
# ============

def potencia_recursiva(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia_recursiva(n,m-1)

# ============
# Ejercicio 4:
# ============

def decimal_a_binario(num):
    """ 
    Recibe int(), 
    Asigna "0","1" según condición
    retorna str()
    """
    binario = ""
    # Caso base, devuelve la variable vacía
    if num <= 0:
        return binario
    
    if num % 2 == 0:
        binario = "0"
        print(binario)
    
    else:
        binario = "1"
        print(binario)

    cociente = num/2
    # Convertir variable a int() para obtener un 0 entero
    cociente = int(cociente)

    return decimal_a_binario(cociente)

def menu():
    print("\n=== Menú ===\n" \
    "1 - Factorial\n" \
    "2 - Fibonacci\n" \
    "3 - Exponente\n" \
    "4 - Convertir a binario\n")


# --------------------------------------------------------------------------

# ================
# Código principal
# ================

# Se utilizan bloques try/except en las llamadas a las funciones
# para evitar el desbordamiento de pila en caso de recursión excesiva.
while True:

    menu()
    opcion = validar_numero("-> ")
    match opcion:

        case 1:
            # ============
            # Ejercicio 1:
            # ============

            print("=== Factorial ===")
            numero = validar_numero("Ingrese un numero, para ver su factorial: ")

            try:
                print(f"El factorial de {numero} es: {factorial_recursivo(numero)}")

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")
        
        case 2:
            # ============
            # Ejercicio 2:
            # ============
            numero = validar_numero("Ingrese un numero para ver la secuencia Fibonacci: ")

            try:
                print(f"\nValor Fibonacci en la posición {numero}: {fibonacci_recursivo(numero)}")
                ver_serie_fibonacci(numero)

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")

        case 3:
            # ============
            # Ejercicio 3:
            # ============
                
            print("\n=== Exponente ===")
            numero = validar_numero("Ingrese número base: ")

            exponente = validar_numero("Ingrese exponente: ")

            numero_potenciado = ""

            try:
                numero_potenciado = potencia_recursiva(numero,exponente)
                print(f"\n{numero} elevado a {exponente} es: {numero_potenciado}\n")

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")

            # Prueba en algoritmo General:
            lista_numero_y_exponente = [
                (2,3),(3,2),(4,4),(6,2),(8,3),(10,4)
            ]
            print("\n=== Prueba de diferentes valores potenciados ===")
            # Se le pasa una lista de valores para probar diferentes combinaciones
            for numero,exponente in lista_numero_y_exponente:
                print(f"\n{numero} elevado a {exponente} es: {potencia_recursiva(numero,exponente)}")

        case 4:
            # ============
            # Ejercicio 4:
            # ============

            print("=== Convertir a número binario ===")

            numero_a_binario = validar_numero("Ingrese número: ")

            try:
                decimal_a_binario(numero_a_binario)

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")
        
        case _:
            print("=== Opción invalida ===")