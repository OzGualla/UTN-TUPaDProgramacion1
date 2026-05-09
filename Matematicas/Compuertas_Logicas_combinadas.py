
# ========================
# Declaración de funciones
# ========================

# Validar números binarios

def validar_binario(mensaje):
    """ Solo acepta un valor binario
        retorna 0/1 (int)"""
    while True:
        try:
            bit = int(input(mensaje))
            if bit in (0, 1):
                return bit
            else:
                print("Único dígito permitido: 0 / 1")
        except ValueError:
            print("Ingrese un número válido")

# Validar números del menú

def validar_numeros():
    """ Recibe como parámetro: numero (str)
    Y retorna: numero (int) validado """
    while True:
        try:
            numero = int(input("Compuerta -> "))
            return numero
        except ValueError:
            print("\nError: Ingrese un número válido")

# para evitar la repetición de pedir input

def pedir_dos_bits():
    """ Devuelve 2 entradas validadas """

    bit_1 = validar_binario("Ingrese el primer bit (0/1): ")
    bit_2 = validar_binario("Ingrese el segundo bit (0/1): ")

    return bit_1, bit_2


"""Funciones de compuertas lógicas"""

# === AND ===
def compuerta_and(bit_1, bit_2):
    # Cada compuerta utiliza condicionales 
    # para simular su funcionamiento
    if bit_1 == 1 and bit_2 == 1:
        salida = 1
    else:
        salida = 0
    return salida


# === OR ===
def compuerta_or(bit_1, bit_2):
    if bit_1 == 1 or bit_2 == 1:
        salida = 1
    else:
        salida = 0
    return salida


# === NAND ===
def compuerta_nand(bit_1, bit_2):
    if bit_1 == 1 and bit_2 == 1:
        salida = 0
    else:
        salida = 1
    return salida


# === NOR ===
def compuerta_nor(bit_1, bit_2):
    if bit_1 == 0 and bit_2 == 0:
        salida = 1
    else:
        salida = 0
    return salida


# === XOR ===
def compuerta_xor(bit_1, bit_2):
    if bit_1 != bit_2:
        salida = 1
    else:
        salida = 0
    return salida

# === NOT ===
def compuerta_not(bit):
    """ Invierte el bit de salida """
    if bit == 1:
        salida = 0
    else:
        salida = 1
    return salida

# Muestra el flujo de la compuerta NOT
def flujo_not(bit, salida):
    print(f"\n{bit} --> [ NOT ] -->  {salida} | Salida |")
    

# Muestra el flujo de las compuerta seleccionada
def flujo_compuerta(bit_1, bit_2, nombre, salida):
    print(f"\n{bit_1} -->\n"\
          f"      [ {nombre} ] -->  {salida} | Salida |\n"\
          f"{bit_2} -->")
    
# === Menú ===
def menu():
    print("\n=== Compuertas lógicas ===")
    print("1 - AND")
    print("2 - OR")
    print("3 - NAND")
    print("4 - NOR")
    print("5 - XOR")
    print("6 - NOT")
    print("0 - Salir")


# ========================
# Estructura principal
# ========================

compuertas = {
    1: {"nombre": "AND",  "funcion": compuerta_and},
    2: {"nombre": "OR",   "funcion": compuerta_or},
    3: {"nombre": "NAND", "funcion": compuerta_nand},
    4: {"nombre": "NOR",  "funcion": compuerta_nor},
    5: {"nombre": "XOR",  "funcion": compuerta_xor},
}

lista_entradas = ["a","b","c","d"]

def main():
    while True:

        entradas = input("\n=== Seleccione cantidad de entradas === \n"\
                        "1 = a \n2 = a, b \n3 = a, b, c \n4 = a, b, c, d\n"\
                        "-> ")
        entradas = int(entradas)
        
        match entradas:
            case 1:
                for a in range(2):
                    resultado = compuerta_not(a)
                    print("\nEntrada a:")
                    flujo_not(a, resultado)

            case 2:
                pass

            case _:
                print("Opción fuera de rango")
        

        # Muestra el menú iterativo
        menu()

        opcion = validar_numeros()
        match opcion:

            case 1:
                print("\n=== AND ===")
                # Se le dan argumentos a la función 
                bit_1, bit_2 = pedir_dos_bits()
                
                # Utilizando el diccionario, se guarda cada valor pedido
                nombre = compuertas[1]["nombre"]
                
                resultado = compuertas[1]["funcion"](bit_1, bit_2)

                # Y le pasa los argumentos a la ultima función para mostrar el flujo
                flujo_compuerta(bit_1, bit_2,nombre, resultado)

            case 2:
                print("\n=== OR ===")

                bit_1, bit_2 = pedir_dos_bits()
                
                nombre = compuertas[2]["nombre"]
                
                resultado = compuertas[2]["funcion"](bit_1, bit_2)

                flujo_compuerta(bit_1, bit_2,nombre, resultado)

            case 3:
                print("\n=== NAND ===")

                bit_1, bit_2 = pedir_dos_bits()
                
                nombre = compuertas[3]["nombre"]
                
                resultado = compuertas[3]["funcion"](bit_1, bit_2)

                flujo_compuerta(bit_1, bit_2,nombre, resultado)

            case 4:
                print("\n=== NOR ===")

                bit_1, bit_2 = pedir_dos_bits()
                
                nombre = compuertas[4]["nombre"]
                
                resultado = compuertas[4]["funcion"](bit_1, bit_2)

                flujo_compuerta(bit_1, bit_2,nombre, resultado)

            case 5:
                print("\n=== XOR ===")

                bit_1, bit_2 = pedir_dos_bits()
                
                nombre = compuertas[5]["nombre"]
                
                resultado = compuertas[5]["funcion"](bit_1, bit_2)

                flujo_compuerta(bit_1, bit_2,nombre, resultado)

            case 6:
                print("\n=== NOT ===")

                bit_1 = validar_binario("Invertir bit (0/1): ")

                resultado = compuerta_not(bit_1)
                
                flujo_not(bit_1, resultado)

            case 0:

                print("\n=== Gracias por su tiempo ===\n")
                break

            case _:

                print("\n=== Opción invalida ===")


if __name__ == "__main__":
    main()
