
""" Tp10 - Recursividad """

# ========================
# Declaración de variables
# ========================

import sys
sys.setrecursionlimit(5000)

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
    
# Validación de entrada:
def validar_numero_y_cero(mensaje):
    """
    Pide input str()
    permite ingresar 0
    Retorna int(validado)
    """
    while True:
        num = input(mensaje)
        if not num.isdigit():
            print("Solo se aceptan números positivos")
            continue

        num = int(num)
        return num
    
# Valida texto
def validar_letras(mensaje):
    while True:
        texto = input(mensaje)
        if not texto.isalpha():
            print("\nSolo se aceptan letras")
            continue
        return texto
    
# ============
# Ejercicio 1:
# ============

def factorial_recursivo(num):
    # Caso Base
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)

# ============
# Ejercicio 2:
# ============

def fibonacci_recursivo(num):
    """ 
    Se recomiendo no ingresar un numero mayor a 40
    para evitar demoras en tiempos de ejecución
    """
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
    # Caso Base
    if m == 0:
        return 1
    else:
        return n * potencia_recursiva(n,m-1)

# ============
# Ejercicio 4:
# ============

def decimal_a_binario(num):
    """ 
    Recibe int() en base decimal, 
    Asigna "0","1" según condición
    retorna str() representado en binario
    """
    # Caso base, devuelve vacío
    if num == 0:
        return ""
    
    resto = str(num % 2)
    # La division entera, es para llegar al numero 0 de forma entera
    cociente = num // 2 
    
    # acumula el resto al final, primero resuelve el cociente
    return decimal_a_binario(cociente) + resto

# ============
# Ejercicio 5:
# ============

def es_palindromo(frase, frase_invertida = "", frase_original = None):
    """
    Recibe str() sin espacios, ni tildes
    Acumula la frase invertida y compara con el original
    Retorna True si es palíndromo, False si no es
    """
    # Guarda la frase solo en la primera llamada
    if frase_original is None:
        frase_original = frase

    # Caso base: compara la frase original con la invertida cuando termina la recursividad acumulada
    if len(frase) == 0:
        return frase_original == frase_invertida
    
    # Agrega la primera letra al frente de frase_invertida y avanza
    return es_palindromo(frase[1:], frase[0] + frase_invertida, frase_original)

# ============
# Ejercicio 6:
# ============
            
def suma_digitos(n):
    """
    Recibe int() positivo
    Retorna int() con la suma de sus dígitos
    Usa % para extraer el último dígito y // para recursion
    """
    # Caso base: un solo dígito, se retorna a sí mismo sin sumar nada
    if n < 10:
        return n
    
    # Extrae el último dígito y suma con el resto
    return (n % 10) + suma_digitos(n // 10)

# ============
# Ejercicio 7:
# ============

def contar_bloques(bloques):
    """
    Recibe int() con cantidad de pisos
    Retorna int() con el total de bloques de la pirámide
    """
    # Case base, si los bloques llegan a 0
    if bloques == 0:
        return 0
    
    else:
        return bloques + contar_bloques(bloques - 1)
    
def dibujar_piramide(piso_actual, total_piso):
    """
    Recibe int() piso actual y total de pisos
    Dibuja cada piso de la pirámide
    """
    # Caso base, si supera el numero total de pisos.
    if piso_actual > total_piso:
        return
    # Imprime los bloques del piso actual
    print("▭ " * piso_actual)

    dibujar_piramide(piso_actual + 1, total_piso)

# ============
# Ejercicio 8:
# ============

def contar_digito(numero, digito):
    """
    Recibe int() numero y int() dígito (0-9)
    Retorna int() con la cantidad de veces que aparece el dígito
    """
    # Caso base: no quedan dígitos
    if numero == 0:
        return 0
    
    # Compara el último dígito con el buscado
    if numero % 10 == digito:
        coincidencia = 1
    else:
        coincidencia = 0
    
    # Descarta el último dígito
    return coincidencia + contar_digito(numero // 10, digito)


# Menú de opciones
def menu():
    print("\n=== Menú ===\n" \
    "1 - Factorial\n" \
    "2 - Fibonacci\n" \
    "3 - Exponente\n" \
    "4 - Convertir a binario\n" \
    "5 - Palíndromo\n" \
    "6 - Suma de dígitos\n" \
    "7 - Pirámide\n" \
    "8 - Contar dígitos\n" \
    "0 - Salir\n")

def siguiente_ejercicio():
    input("\nPresione una tecla para continuar...")

# --------------------------------------------------------------------------

# ================
# Código principal
# ================

# Se utilizan bloques try/except en las llamadas a las funciones
# para evitar el desbordamiento de pila en caso de recursión excesiva.
while True:

    menu()
    opcion = validar_numero_y_cero("-> ")
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
            
            siguiente_ejercicio()
        
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
            
            siguiente_ejercicio()

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
            print(lista_numero_y_exponente)
            # Se le pasa una lista de valores para probar diferentes combinaciones
            for numero,exponente in lista_numero_y_exponente:
                print(f"\n{numero} elevado a {exponente} es: {potencia_recursiva(numero,exponente)}")
            
            siguiente_ejercicio()

        case 4:
            # ============
            # Ejercicio 4:
            # ============

            print("=== Convertir a número binario ===")

            numero_a_binario = validar_numero("Ingrese número a convertir: ")

            try:
                resultado = decimal_a_binario(numero_a_binario)
                print(f"{numero_a_binario} en binario es: {resultado}")

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")
            
            siguiente_ejercicio()

        case 5:
            # ============
            # Ejercicio 5:
            # ============
            print("=== Palíndromo ===")
            print("Ingrese una frase (sin espacios, ni tildes) para saber si es Palíndromo")
            # Uso funcion .lower() y .strip() para evitar inconsistencias en la frase
            frase = validar_letras("Frase: ").lower().strip()
            
            try:
                # Muestra True or False según coincidencia
                print(f"{frase} es Palíndromo?\n-> {es_palindromo(frase)}")

            except RecursionError:
                print(f"\nError: Se ha sobrepasado el limite de pila")
            
            siguiente_ejercicio()

        case 6:
            # ============
            # Ejercicio 6:
            # ============
                print("=== Suma de dígitos ===")
                numero = validar_numero("Ingrese un número: ")

                try:
                    print(f"Suma de dígitos de {numero}: {suma_digitos(numero)}")

                except RecursionError:
                    print("\nError: Se ha sobrepasado el límite de pila")
        
        case 7:
            # ============
            # Ejercicio 7:
            # ============
            print("=== Pirámide de bloques ===")

            print("Cuantos bloques puso el niño en el nivel inferior?")
            cantidad_bloques = validar_numero("Bloques -> ") 
            
            try:
                total = contar_bloques(cantidad_bloques)
                print(f"\nEntonces va a necesitar {contar_bloques(cantidad_bloques)} bloques\n"\
                    "para construir la pirámide")

                print("\n=== Pirámide ===\n")
                dibujar_piramide(1, cantidad_bloques)
                
            except RecursionError:
                    print("\nError: Ha puesto demasiados bloques! no podrá construir la pirámide")
            
            siguiente_ejercicio()

        case 8:
            # ============
            # Ejercicio 8:
            # ============
            numero = validar_numero("Ingresá un número: ")
            digito = validar_numero("Ingresá un dígito (1-9): ")

            try:
                resultado = contar_digito(numero, digito)
                print(f"El dígito {digito} aparece {resultado} vez/veces en {numero}")
            except RecursionError:
                print("\nError: Se ha sobrepasado el límite de pila")
        
        case 0:
            print("=== Gracias por su tiempo ===")
            break
        
        case _:
            print("=== Opción invalida ===")