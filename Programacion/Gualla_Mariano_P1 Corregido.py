"""
Sistema de stock para ferretería:
- Carga de herramientas
- Asignar cantidad
- Consultar stock
- Actualizar inventario
"""
# ===================
# Bloque de funciones 
# ===================
def validar_letras(palabra):
    """
    Recibe como parámetro: palabra (str)
    Y retorna: palabra (str) validado
    """
    while not palabra.isalpha():
        print("\nSolo se aceptan letras")
        palabra = input("Ingrese nuevamente: ")
    return palabra

# Para validar números negativos
def validar_no_acepta_n_negativos(numero):
    """
    Si el parámetro comienza con "-"
    ignora ese carácter y verifica si la entrada no es un dígito
    si no lo es no acepta la entrada y vuelve a pedir el input.
    VALIDA NÚMEROS NEGATIVOS PERO NO LOS ACEPTA COMO ENTRADA
    Recibe como parámetro: numero (str)
    Y retorna: numero (int) validado
    """
    while True:
        # Validar que sea número (permite "-")
        if numero.lstrip("-").isdigit():
            numero = int(numero)

            # Validar que NO sea negativo
            if numero < 0:
                print("Error: No se puede ingresar una cantidad menor a 0")
                numero = input("Ingrese nuevamente: ")
            else:
                return numero
        else:
            print("Solo se aceptan números")
            numero = input("Ingrese nuevamente: ")

# Pausa la ejecución hasta que el usuario presiona una tecla
def pausar_programa():
    input("Presione una tecla para continuar. ")

# ===================
# Programa principal 
# ===================

# Declaración de listas a utilizar, que compartirán índice 
# para asociar cada herramienta con su cantidad de stock
herramientas = []
existencias = []

opcion = ""
count_opcion_1 = True
count_opcion_2 = True

# Menú iterativo, se repite hasta que el usuario seleccione la opción de salir (8)
while opcion != 8:
    while True:
        print("-"*65)
        print("\n---- Sistema de Stock ----")
        print("\n1 - Carga inicial de herramientas\n"\
            "2 - Carga de existencias\n"\
            "3 - Visualización de inventario\n"\
            "4 - Consulta de stock\n"\
            "5 - Reporte de agotados\n"\
            "6 - Alta de nuevo producto\n"\
            "7 - Actualización de stock\n"\
            "8 - Salir")
        opcion = validar_no_acepta_n_negativos(input("-> "))

        # Selección de menú según input
        # Finalizar ejecucion del programa
        if opcion == 8:
            print("Sistema Cerrado")
            break
        
        elif opcion == 1: # Carga inicial de herramientas
            print("\n--- Carga de herramientas ---")

            if not count_opcion_1:
                 print("Ya se ha realizado la carga inicial de herramientas")
                 break
            count_opcion_1 = False

            while True: 
                cantidad_herramientas = validar_no_acepta_n_negativos(input("Ingrese cantidad -> "))
                if cantidad_herramientas <= 0:
                    print("Error: El ingreso debe ser mayor a 0")
                    continue
                break

            for i in range(cantidad_herramientas):
                while True:
                    herramienta_ingresada = validar_letras(input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip())
                    
                    # Valido que el elemento ingresado no exista actualmente en la lista, para evitar repeticiones
                    if herramienta_ingresada in herramientas:
                        print(f"Ya se a registrado la herramienta {herramienta_ingresada.capitalize()}")
                        continue
                    break
                herramientas.append(herramienta_ingresada)

        elif opcion == 2: # Carga de Existencias
            print("\n--- Carga de existencias ---")
            # Si la lista herramientas se encuentra vacía, te devuelve al menú principal

            if herramientas == []:
                    print("-"*65)
                    print("\nError: Aún no se registraron herramientas:\n"\
                            "Por favor, primero registre herramientas.")
                    continue
            
            if not count_opcion_2:
                 print("Ya se ha realizado la carga inicial de existencias")
                 break
            count_opcion_2 = False

            for i in range(len(herramientas)):
                print("\n--- Carga de Existencias ---")

                cantidad_existencias = validar_no_acepta_n_negativos(input("Ingrese la cantidad de unidades\n"\
                f"para la herramienta: {herramientas[i]} -> "))

                # Aseguro que se comparte el índice con la lista herramientas
                # Ingresando en el mismo orden ambos elementos
                existencias.append(cantidad_existencias)
                # Con cada ingreso, se muestra la herramienta junto a su stock asociado
                print(f"\nStock asignado a {herramientas[i]}: {existencias[i]} unidades")

        elif opcion == 3: # Visualización de Inventario
            # Si no se registraron herramientas, vuelve al menú
            if herramientas == []:
                print("\nInventario vacío. por favor Registre herramientas")
                continue
            # Si se registraron herramientas pero no se ingresaron existencias
            # al momento de seleccionar esta opción, vuelve al menú mostrando el error correspondiente
            if existencias == []:
                print("\nError: herramientas sin stock disponible\n"\
                        "Por favor, primero asigne stock a las herramientas")
                continue

            print("\n--- Inventario Actual ---\n"\
                    "-----------------------")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]} unidades")

            pausar_programa()
            
        elif opcion == 4: # Consulta de Stock
            print("--- Consulta de Stock ---")

            if herramientas == []:
                print("\nInventario vacío. por favor Registre herramientas")
                continue
            
            if existencias == []:
                print("\nError: herramientas sin stock disponible\n"\
                        "Por favor, primero asigne stock a las herramientas")
                continue

            buscar_herramienta = validar_letras(input("Ingrese el nombre de la herramienta que quiera consultar: ").strip())
            
            if buscar_herramienta in herramientas:
                # Se guarda el índice asociado
                herramienta_encontrada = herramientas.index(buscar_herramienta)
                # Y se utiliza esta variable para recorrer la lista paralela y asociar el indice con la cantidad de stock
                print(f"\n{buscar_herramienta.capitalize()}, Stock actual: {existencias[herramienta_encontrada]}\n")
                pausar_programa()
            else:
                    print("\nLa herramienta solicitada no existe en el catalogo")
                    pausar_programa()

        elif opcion == 5: # Reporte de Agotados
            print("--- Reporte de Agotados ---")

            if herramientas == []:
                print("\nInventario vacío. por favor Registre herramientas")
                continue
            
            if existencias == []:
                print("\nError: herramientas sin stock disponible\n"\
                        "Por favor, primero asigne stock a las herramientas")
                continue

            for i in range(len(existencias)):
                if existencias[i] == 0:
                    # Lo imprime por pantalla junto al elemento asociado en la lista paralela
                    # de esta forma logrando visualizar solo las herramientas con stock 0
                    print(f"{herramientas[i]}: {existencias[i]} unidades")
            pausar_programa()

        elif opcion == 6: # Alta de Nuevo Producto

            if herramientas == []:
                print("\nPrimero realize una carga inicial de herramientas")
                continue

            if existencias == []:
                print("\nError: herramientas sin stock disponible\n"\
                        "Por favor, primero asigne stock a las herramientas")
                continue

            print("--- Alta de nuevo producto ---")
            while True:
                # Se permite ingresar un nuevo elemento a la lista herramientas
                nueva_herramienta = validar_letras(input("Ingrese nombre de nueva herramienta: ").strip())
                # Si este elemento ya se encuentra, se vuelve al menú de opciones
                if nueva_herramienta in herramientas:
                    print("\nError: La herramienta ya se encuentra en Stock")
                    continue
                break
            
            nueva_existencia = validar_no_acepta_n_negativos(input(f"Ingrese stock de {nueva_herramienta.capitalize()}: "))

            # Por último se agregan los elementos a sus listas e índices correspondientes
            # Asegurando de esta forma, que compartirán índice
            herramientas.append(nueva_herramienta)
            existencias.append(nueva_existencia)
                
            print("\nNueva herramienta registrada")
            pausar_programa()

        elif opcion == 7: # Actualización de Stock
            print("\n--- Actualización de Stock ---")

            seleccion_herramienta = ""
            venta_herramienta = ""

            # Si la lista herramientas o existencias están vacías
            # No permite ingresar al apartado de actualización de stock
            if herramientas == []:
                    print("-"*65)
                    print("\nError: Aún no se registraron herramientas:\n"\
                        "Por favor, primero registre herramientas.")
                    continue
            
            if existencias == []:
                    print("-"*65)
                    print("\nError: herramientas sin stock disponible\n"\
                        "Por favor, primero asigne stock a las herramientas")
                    continue
            
            actualizacion = validar_no_acepta_n_negativos(input("1 - Ventas\n2 - Ingreso\n3 - Volver\n-> "))

            if actualizacion == 1:
                print("\nVenta - Seleccione herramienta:")
                print("-"*30)

                while True:
                    for i in range(len(herramientas)):
                        print(f"{herramientas[i]} - Stock: {existencias[i]}")    
                    seleccion_herramienta = validar_letras(input("-> ").strip())
                    
                    if seleccion_herramienta not in herramientas:
                        print("\nLa herramienta no se encuentra disponible en el catálogo, ingrese nuevamente:\n")
                        continue

                    break

                # Si la herramienta selecciona no dispone de stock (0) no se permite la venta
                # y te devuelve al menú 
                indice_paralelo = herramientas.index(seleccion_herramienta)
                if existencias[indice_paralelo] <= 0:
                    print("\nNo se puede realizar la venta,\nla herramienta no cuenta con stock actual")
                    pausar_programa()
                    continue

                while True:
                    venta_herramienta = validar_no_acepta_n_negativos(input("Ingrese cantidad vendida: "))

                    # La venta no puede ser 0 
                    if seleccion_herramienta <= 0:
                        print("Error: Las ventas deben ser mayor a 0")
                        continue

                    # no se permite vender un item si no hay stock suficiente
                    if venta_herramienta > existencias[indice_paralelo]:
                        print("\nLa cantidad vendida supera el stock actual\n")
                        print("Intente de nuevo")
                        continue
                    
                    break
                # Utilizando el indice dentro de la lista existencias,
                # se le resta y reasigna el numero ingresado a este elemento
                existencias[indice_paralelo] -= venta_herramienta
                print(f"\nSe ha vendido {herramientas[indice_paralelo]} por {venta_herramienta} unidades")
                pausar_programa()

            elif actualizacion == 2:
                print("\nIngreso de stock - Seleccione herramienta:")
                print("-"*30)
                for i in range (len(herramientas)):
                    print(f"{herramientas[i]} - Stock: {existencias[i]}")
                
                while True:
                    seleccion_herramienta = validar_letras(input("-> ").strip())
                    
                    if not seleccion_herramienta in herramientas:
                        print("\nLa herramienta no se encuentra disponible en el catálogo, ingrese nuevamente\n")
                        continue
                    break
                
                indice_paralelo = herramientas.index(seleccion_herramienta)
                
                while True:
                    aumentar_stock = validar_no_acepta_n_negativos(input("Ingrese cantidad a agregar al stock: "))
                    # La venta no puede ser 0 
                    if seleccion_herramienta <= 0:
                        print("Error: Las ventas deben ser mayor a 0")
                        continue
                    break

                # Utilizando el indice dentro de la lista existencias,
                # se le suma y reasigna el numero ingresado a este elemento
                existencias[indice_paralelo] += aumentar_stock
                print("Cantidad agregada correctamente")
                
            elif actualizacion == 3:
                continue

        else:
            print("-"*65)
            print("\nError: Opción inválida\n"\
                    "Seleccione una opción del menú")

