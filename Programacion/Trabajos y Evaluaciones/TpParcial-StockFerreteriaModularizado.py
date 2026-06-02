
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
    Retorna int(validado)
    """
    while True:

        try:
            numero = input(mensaje)

            if not numero.strip("-").isdigit():

                raise ValueError("Error: Solo se aceptan números")
            
            numero = int(numero)

            return numero
        
        except ValueError as error:

            print(f"Error: {error}\n")
            
            continue


def validar_letras(mensaje):
    """
    Solicita una cadena al usuario y valida
    que contenga únicamente letras y espacios.
    """
    while True:

        try:
            palabra = input(mensaje).strip()

            # Regla de negocio:
            # no permitir nombres vacíos
            if not palabra:

                raise ValueError("El campo no puede estar vacío")

            # Validar que solo contenga letras y espacios
            if not palabra.replace(" ", "").isalpha():

                raise ValueError("Solo se aceptan letras")
            
            return palabra
        
        except ValueError as error:

            print(f"Error: {error}")


def inventario_vacio(inventario):
    """
    Comprueba si el inventario esta vació
    y da aviso al usuario
    """
    if not inventario:

        print("\nEl inventario se encuentra vació\n"\
            "----------------------------------------\n"
            "Para hacer un carga inicial de herramientas\n"\
            "Utilize la opción 1 - Carga de Herramientas")
        
        return True
    
    return False


# Buscar herramienta en la lista
def buscar_herramienta(inventario, nombre):

    for item in inventario:

        if(item['herramienta'].strip().lower() == nombre.strip().lower()):

            return item

    return None


# Funcionalidad 1: cargar herramientas al sistema
def cargar_herramientas(inventario):
    """
    Permite cargar herramientas con stock inicial
    únicamente si el inventario está vacío.
    """

    # Regla de negocio:
    # no permitir recargar el inventario inicial
    
    if inventario:
            
            print("\nEl inventario ya contiene herramientas\n"\
            "----------------------------------------\n"
            "Para cargar una nueva herramientas\n"\
            "Utilize la opción 5 - Alta de Nuevo Producto")
        
            return

    while True:

        cantidad_herramientas = validar_numero("Ingrese la cantidad de herramientas a cargar: ")

        if cantidad_herramientas <= 0:

            print("Error: La cantidad no puede ser menor o igual a 0")

            continue

        break

    # Cargar exactamente la cantidad indicada
    for herramienta in range(cantidad_herramientas):

        while True:

            try:
                nombre_herramienta = validar_letras(f"\nIngrese nombre de herramienta n°{herramienta + 1}/{cantidad_herramientas}: ")

                # Comparar nombres
                if any(item['herramienta'].lower() == nombre_herramienta.lower() for item in inventario):

                    raise ValueError("La herramienta ya se encuentra registrada")

                break

            except ValueError as error:

                print(f"\nError: {error}")

        # El stock inicial puede ser 0
        while True:

            stock_inicial = validar_numero(f"Ingrese stock inicial de {nombre_herramienta}: ")

            if stock_inicial < 0:

                print("El stock no puede ser menor o igual a 0")

                continue

            break

        # Crear diccionario temporal
        dict_temp = {
            "herramienta": nombre_herramienta,
            "cantidad": stock_inicial
        }

        # Agregar herramienta al inventario
        inventario.append(dict_temp)

        print(f"Herramienta cargada con éxito: {nombre_herramienta} | Stock: {stock_inicial}")


# Funcionalidad 2: Visualizar inventario
def visualizar_inventario(inventario):
    """
    Muestra todas las herramientas registradas, junto a su stock
    """
    # No se puede visualizar el inventario si este se encuentra vació
    if inventario_vacio(inventario):
        return
    
    print("=== Inventario ====")
    # Recorrer y mostrar cada herramienta registrada

    for item in inventario:

        print(f"{item['herramienta']} | Stock: {item['cantidad']}")
    

# Funcionalidad 3: Consultar stock de una herramienta
def consultar_stock(inventario):
    """
    Permite buscar una herramienta en el inventario
    y mostrar su stock actual.
    """
    # Verificar que el inventario no este vació
    if inventario_vacio(inventario):
        return
    
    # Solicitar nombre de herramienta
    buscar_herramienta = validar_letras("Ingrese nombre de herramienta: ")

    # Bandera para verificar si la herramienta existe
    herramienta_encontrada = False

    # Buscar herramienta en el inventario
    for item in inventario:

        if buscar_herramienta.strip().lower() == item['herramienta'].lower():

            print(f"Herramienta: {item['herramienta']} | Stock: {item['cantidad']}")

            herramienta_encontrada = True

            break

    # Informar si la herramienta no existe
    if not herramienta_encontrada:

        print("Error: La herramienta no existe en el inventario")


# Funcionalidad 4: Reporte de stocks agotados
"""
Buscar todos los stock con valor 0
y los muestra por pantalla
"""
def reportar_agotados(inventario):

    if inventario_vacio(inventario):
        return
    
    # Buscar cantidad con valor 0 en el inventario
    for item in inventario:

        if item['cantidad'] == 0:

            print(f"{item['herramienta']} | Stock: {item['cantidad']}")


# Funcionalidad 5: Alta nuevo producto
def alta_producto(inventario):

    if inventario_vacio(inventario):

        return

    try:

        nueva_herramienta = input("Ingrese el nombre de la nueva herramienta: ").strip()

        # Verificar nombre vació o con caracteres no permitidos
        if not nueva_herramienta.replace(" ", "").isalpha():
                
                raise ValueError("Solo se aceptan letras, y el campo no puede estar vació\n"\
                            "=== Volviendo al menú principal ===")
        
        # Verificar duplicados
        if any(nueva_herramienta.strip().lower() == item['herramienta'].strip().lower() for item in inventario):

            raise ValueError(f"La herramienta {nueva_herramienta} ya se encuentra registrada\n"\
                            "=== Volviendo al menú principal ===")
        
        stock_inicial = validar_numero(f"Ingrese stock inicial de {nueva_herramienta}: ")

        # Verificar stock mayor a 0
        if stock_inicial < 0:
            
            raise ValueError(f"El Stock no puede ser menor a 0\n"\
                            "=== Volviendo al menú principal ===")
        
        # En todos los casos, volverá al menu si se ejecuta el raise

        # Se crea un dict temporal para almacenar clave: valor
        dict_temp = {
            "herramienta": nueva_herramienta,
            "cantidad": stock_inicial
        }

        # Se guarda la nueva herramienta con su stock inicial 
        inventario.append(dict_temp)
        
    except ValueError as error:
        print(f"Error: {error}")


# Funcionalidad 6: Actualizar Stock (Venta e ingreso)        
def actualizar_stock(inventario):

    if inventario_vacio(inventario):
        return
    
    for item in inventario:
        print(f"{item['herramienta']} | Stock: {item['cantidad']}")

    print("\n1 - Venta\n"\
        "2 - Ingreso")
    
    while True:
        opcion = validar_numero("Seleccionar opción -> ")

        match opcion:

            case 1:

                print("=== Venta ===\n")

                try:

                    buscar = validar_letras("Seleccione herramienta: ")

                    herramienta = buscar_herramienta(inventario, buscar)

                    if herramienta is None:

                        raise ValueError("La herramienta no se encuentra en el catálogo")
                
                    cantidad_venta = validar_numero("Cantidad vendida: ")

                    if cantidad_venta <= 0:

                        raise ValueError("La cantidad no puede ser menor o igual a 0")
                    
                    if cantidad_venta > item['cantidad']:

                        raise ValueError("La cantidad vendida supera el stock actual")

                    item['cantidad'] -= cantidad_venta

                    print(f"=== Se han vendido {cantidad_venta} unidades de {item['herramienta']} ===")

                    print(f"Actualización de herramienta: {item['herramienta']} | Stock actual: {item['cantidad']}")

                except ValueError as error:
                    print(f"Error: {error}")
                
                break

            case 2:

                print("=== Ingreso ===\n")
                
                try:

                    buscar = validar_letras("Seleccione herramienta: ")

                    herramienta = buscar_herramienta(inventario, buscar)

                    if herramienta is None:

                        raise ValueError("La herramienta no se encuentra en el catálogo")
                
                    cantidad_ingreso = validar_numero("Cantidad ingresada: ")

                    if cantidad_ingreso <= 0:

                        raise ValueError("La cantidad no puede ser menor o igual a 0")

                    item['cantidad'] += cantidad_ingreso

                    print(f"=== Se han ingresado {cantidad_ingreso} unidades de {item['herramienta']} ===")
                    
                    print(f"Actualización de herramienta: {item['herramienta']} | Stock actual: {item['cantidad']}")

                except ValueError as error:
                    print(f"Error: {error}")
                
            case _:
                print("=== Opción Invalida")

    pass


# Menú iterativo
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


def pausar_ejecucion():
    """ Realiza una pausa, hasta que el usuario ingrese una tecla """
    input("\nPresione una tecla para continuar...")


def main():

    # Lista donde se almacenaran los diccionarios
    inventario = []

    while True:

        menu()  

        print("Seleccione operación:")
        opcion = validar_numero("-> ")

        match opcion:

            case 1:

                cargar_herramientas(inventario)

                pausar_ejecucion()

            case 2:
                
                visualizar_inventario(inventario)

                pausar_ejecucion()

            case 3:
                
                consultar_stock(inventario)

                pausar_ejecucion()

            case 4:
                
                reportar_agotados(inventario)

                pausar_ejecucion()

            case 5:
                
                alta_producto(inventario)

                pausar_ejecucion()

            case 6:

                actualizar_stock(inventario)

                pausar_ejecucion()

            case 0:
                print("=== Gracias por su tiempo ===")
                break
            
            case _:
                print("=== Opción inválida ===")

                pausar_ejecucion()

if __name__=="__main__":
    main()