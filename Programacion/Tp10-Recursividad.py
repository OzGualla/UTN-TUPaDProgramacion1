
""" Tp10 - Recursividad """

# ========================
# Declaración de variables
# ========================

# Validación de entradas
def validar_numero(mensaje):
    """
    Pide input str()
    Retorna int(validado)
    """
    while True:
        num = input(mensaje)
        if not num.isdigit():
            print("Solo se aceptan numeros positivos")
            continue

        num = int(num)
        if num <= 0:
            print("Error: El numero no puede ser igual o menor a 0")
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

def potencia_recursiva(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia_recursiva(n,m-1)

# ============
# Ejercicio 3:
# ============

def decimal_a_binario(num):
    """ 
    Recibe int(), 
    Asigna "0","1" segun condicion
    retorna str()
    """
    binario = ""
    # Caso base, devuelve la variable vacia
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
    "2 - Exponente\n" \
    "3 - Conversor binario\n")


# --------------------------------------------------------------------------

# ================
# Código principal
# ================

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

            print(f"El factorial de {numero} es: {factorial_recursivo(numero)}")

        case 2:
            # ============
            # Ejercicio 2:
            # ============
                
            print("\n=== Exponente ===")
            numero = validar_numero("Ingrese número base: ")

            exponente = validar_numero("Ingrese exponente: ")

            numero_potenciado = potencia_recursiva(numero,exponente)

            print(f"\n{numero} elevado a {exponente} es: {numero_potenciado}\n")

        case 3:
            # ============
            # Ejercicio 3:
            # ============

            print("=== Convertir a número binario ===")

            numero_a_binario = validar_numero("Ingrese número: ")
            decimal_a_binario(numero_a_binario)
        
        case _:
            print("=== Opcion invalida ===")