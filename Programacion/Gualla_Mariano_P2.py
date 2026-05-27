
"""
Sistema de stock para ferretería:
- Carga de herramientas
- Asignar cantidad
- Consultar stock
- Actualizar inventario
"""
# ========================
# Declaración de funciones
# ========================

# Validación de entradas
def validar_numero(mensaje):
    """
    Pide input str()
    No acepta 0 como valor
    Retorna int(validado)
    """
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if numero <= 0:
                print("Error: El número no puede ser igual o menor a 0")
                continue
            return numero
        
        except ValueError:
            print("Error: Solo se aceptan números")
            continue


def validar_numero_y_cero(mensaje):
    """
    Pide input str()
    permite ingresar 0
    Retorna int(validado)
    """
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            return numero
        
        except ValueError:
            print("Error: Solo se aceptan números")
            continue


def validar_letras(mensaje):
    while True:
        try:
            palabra = input(mensaje)

            if not palabra.isalpha():
                # Lanza una excepción si el dato no cumple la validación
                raise ValueError("Solo se aceptan letras")

            return palabra

        except ValueError as error:
            print(f"Error: {error}")

# Funcionalidad 1: cargar herramientas al sistema
def cargar_herramientas(inventario):
    """
    Permite cargar n cantidad de herramientas
    con su stock inicial en una lista de diccionarios
    solo si la lista se encuentra vacía
    """
    # Verificar que la lista se encuentre vacía para permitir la carga inicial

    try:
        # Regla de negocio:
        # no permitir recargar el inventario inicial
        if inventario:
            raise ValueError("Error: El inventario ya contiene herramientas\n\n"\
                            "Para cargar una nueva herramienta\n"\
                            "utilize la opción 5 - Alta de Nuevo Producto")
        
        cantidad_herramientas = validar_numero("Ingrese la cantidad de herramientas a cargar: ")
        
        # Agregar cantidad de herramientas igual las requeridas por el usuario
        for herramienta in range(cantidad_herramientas):

            while True:

                nombre_herramienta = validar_letras(f"\nIngrese nombre de herramienta n°{herramienta+1}/{cantidad_herramientas}: ").strip()
                # Recorre y Compara si algún valor de las claves "herramienta" es igual al input
                if any(item["herramienta"] == nombre_herramienta for item in inventario):
                    print("Error: La herramienta ya se encuentra registrada")
                    continue

                break

            stock_inicial = validar_numero_y_cero(f"Ingrese stock inicial de {nombre_herramienta}: ")
            # Crear un diccionario temporal para agregarlo a la lista inventario

            dict_temp = {
            # Las claves serán "herramienta" y "cantidad"
            "herramienta": nombre_herramienta,
            "cantidad": stock_inicial
            }

            # Agregar el diccionario a la lista inventario
            inventario.append(dict_temp)
            # Se notifica al usuario que la herramienta se cargo con éxito
            print(f"Herramienta cargada con éxito: {nombre_herramienta} | Stock: {stock_inicial}")
    
    except ValueError as error:
        print(f"\nError: {error}")
        
    
def menu():
    print("""\n
================ Sistema de Stock ================
1 - Carga de Herramientas con Existencias Iniciales
2 - Visualización de Inventario
3 - Consulta de Stock
4 - Reporte de Agotados
5 - Alta de Nuevo Producto
6 - Actualización de Stock (Venta / Ingreso)
0 - Salir\n""")

def siguiente_ejercicio():
    input("\nPresione una tecla para continuar...")

def main():

    # Lista donde se almacenaran los diccionarios
    inventario = []

    while True:

        menu()  

        opcion = validar_numero_y_cero("-> ")

        match opcion:

            case 1:

                cargar_herramientas(inventario)

                siguiente_ejercicio()

            case 2:
                pass
            case 3:
                pass
            case 5:
                pass
            case 4:
                pass

            case 0:
                print("=== Gracias por su tiempo ===")
                break
            
            case _:
                pass

if __name__=="__main__":
    main()