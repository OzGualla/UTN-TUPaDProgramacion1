
# Declaración de listas a utilizar, que compartirán índice 
# para asociar cada herramienta con su cantidad de stock
herramientas = []
existencias = []
# Declaración de variables a utilizar
cantidad_herramientas = ""
cantidad_existencias = ""
opcion = ""

# Menú iterativo, se repite hasta que el usuario seleccione la opción de salir (8)
while opcion != 8:
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
    opcion = input("-> ")
    # Verificación de menú, solo se aceptan números
    # Vuelvo a mostrar el menú, solo para evitar tener que volver hacia arriba para ver las opciones
    # En caso de ingresar varias entradas inválidas
    while not opcion.isdigit():
        print("-"*65)
        print("Error: Opción inválida\nSolo se aceptan números")
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
        opcion = input("-> ")
    
    opcion = int(opcion)

    # Selección de menú según input
    if opcion == 1: # Carga inicial de herramientas

        print("\n--- Carga de herramientas ---")
        while True:
                cantidad_herramientas = input("Ingrese cantidad -> ")
                # Si se ingresa un "-" al principio,
                # Lo quito temporalmente, solo para validar si
                # La entrada es un dígito
                # Si no es un dígito, se saltea el siguiente bloque
                # Y vuelve a ejecutar 
                if not cantidad_herramientas.lstrip("-").isdigit():
                    print("Error: Solo se aceptan números")
                    continue
                # Si resulta ser un dígito, lo convierto a entero
                cantidad_herramientas = int(cantidad_herramientas)
                # Para luego validar si el numero es negativo
                if cantidad_herramientas <= 0:
                    print("Error: El ingreso debe ser mayor a 0\nY no se aceptan números negativos")
                    continue
                # Aclaro que este procedimiento lo llevo a cabo para cumplir con la consigna 
                # "Validar que las existencias ingresadas sean números enteros positivos o cero."
                break

        for i in range(cantidad_herramientas):
            while True:
                herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip()
                if not herramienta_ingresada.isalpha():
                    print("Error: Solo se aceptan letras")
                    continue
                # Valido que el elemento ingresado no exista actualmente en la lista, para evitar repeticiones
                if herramienta_ingresada in herramientas:
                    print(f"Ya se a registrado la herramienta {herramienta_ingresada.capitalize()}")
                    continue
                break
            herramientas.append(herramienta_ingresada)

    elif opcion == 2: # Carga de Existencias
        # Si la lista herramientas se encuentra vacía, te devuelve al menú principal
        if herramientas == []:
                print("-"*65)
                print("\nError: Aún no se registraron herramientas:\n"\
                        "Por favor, primero registre herramientas.")
                continue

        for i in range(cantidad_herramientas):
            print("\n--- Carga de Existencias ---")
            while True:  
                cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                    f"para la herramienta: {herramientas[i]} -> ")
                
                if not cantidad_existencias.lstrip("-").isdigit():
                        print("Error: Solo se aceptan números enteros o 0")
                        continue
                
                cantidad_existencias = int(cantidad_existencias)
                # Verificación, Si el número es negativo, se vuelve a pedir el ingreso
                if cantidad_existencias < 0:
                    print("Error: No se puede ingresar una cantidad negativa")
                    continue
                break
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

        # Este input es solo para poder visualizar el inventario, 
        # Sin que la vista del menú iterable moleste al usuario
        input("\nPresione una tecla, para volver al menú.")

    elif opcion == 4: # Consulta de Stock
        print("--- Consulta de Stock ---")

        if herramientas == []:
            print("\nInventario vacío. por favor Registre herramientas")
            continue
        
        if existencias == []:
            print("\nError: herramientas sin stock disponible\n"\
                    "Por favor, primero asigne stock a las herramientas")
            continue

        buscar_herramienta = input("Ingrese el nombre de la herramienta que quiera consultar: ")
        while not buscar_herramienta.isalpha():
                print("\nSolo se aceptan letras")
                buscar_herramienta = input("Ingrese el nombre de la herramienta que quiera consultar: ")
        # Si el nombre ingresado coincide con la lista
        if buscar_herramienta in herramientas:
            # Se guarda el índice asociado
            herramienta_encontrada = herramientas.index(buscar_herramienta)
            # Y se utiliza esta variable para recorrer la lista paralela y asociar el indice con la cantidad de stock
            print(f"\n{buscar_herramienta.capitalize()}, Stock actual: {existencias[herramienta_encontrada]}\n")
            input("\nPresione una tecla, para volver al menú.")
        else:
                print("\nLa herramienta solicitada no existe en el catalogo")
                input("\nPresione una tecla, para volver al menú.")

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
        input("\nPresione una tecla, para volver al menú.")

    elif opcion == 6: # Alta de Nuevo Producto
        print("--- Alta de nuevo producto ---")
        while True:
            # Se permite ingresar un nuevo elemento a la lista herramientas
            nueva_herramienta = input("Ingrese nombre de nueva herramienta: ").strip()
            # Si este elemento ya se encuentra, se vuelve al menú de opciones
            if nueva_herramienta in herramientas:
                print("\nError: La herramienta ya se encuentra en Stock")
                continue
            # Verifico que solo se ingresen letras
            if not nueva_herramienta.isalpha():
                print("Error: Solo se aceptan letras")
                continue
            break
        
        while True:
            nueva_existencia = input(f"Ingrese stock de {nueva_herramienta.capitalize()}: ")
            # Si no es un número, se vuelve al menú de opciones
            if not nueva_existencia.lstrip("-").isdigit():
                print("Error: No se ha ingresado un número")
                continue
            nueva_existencia = int(nueva_existencia)

            if nueva_existencia < 0:
                # Si nueva_existencia es menor a 0, se vuelve al menú de opciones
                print("Error: No se puede agregar una cantidad menor a 0")
                continue
            # Por último se agregan los elementos a sus listas e índices correspondientes
            # Asegurando de esta forma, que compartirán índice
            herramientas.append(nueva_herramienta)
            existencias.append(nueva_existencia)
            break
            
        print("\nNueva herramienta registrada")
        input("\nPresione una tecla, para volver al menú.")

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
        
        actualizacion = input("1 - Ventas\n2 - Ingreso\n3 - Volver\n-> ")

        while not actualizacion.isdigit():
                print("Error: Solo se aceptan números")
                actualizacion = input("1 - Ventas\n2 - Ingreso\n3 - Volver\n-> ")

        actualizacion = int(actualizacion)

        if actualizacion == 1:
            print("\nVenta - Seleccione herramienta:")
            print("-"*30)

            while True:
                for i in range(len(herramientas)):
                    print(f"{herramientas[i]} - Stock: {existencias[i]}")    
                seleccion_herramienta = input("-> ").strip()
                     
                if not seleccion_herramienta.isalpha():
                    print("Error: Solo se aceptan letras")
                    continue
                
                if seleccion_herramienta not in herramientas:
                    print("\nLa herramienta no se encuentra disponible en el catalogo, ingrese nuevamente:\n")
                    continue

                break

            # Si la herramienta selecciona no dispone de stock (0) no se permite la venta
            # y te devuelve al menú 
            indice_paralelo = herramientas.index(seleccion_herramienta)
            if existencias[indice_paralelo] <= 0:
                print("No se puede realizar la venta,\nla herramienta no cuenta con stock actual")
                continue

            while True:
                venta_herramienta = input("Ingrese cantidad vendida: ")
                if not venta_herramienta.lstrip("-").isdigit():
                    print("Error: Solo se aceptan números")
                    continue
                
                venta_herramienta = int(venta_herramienta)

                # no se permite vender una cantidad menor o igual a 0
                if venta_herramienta <= 0:
                    print("Error: Las ventas deben ser mayor a 0\nNo se aceptan números negativos")
                    continue
                # no se permite vender un item si no hay stock suficiente
                if venta_herramienta > existencias[indice_paralelo]:
                    print("La cantidad vendida supera el stock actual\n")
                    print("Intente de nuevo")
                    continue
                
                break
            # Utilizando el indice dentro de la lista existencias,
            # se le resta y reasigna el numero ingresado a este elemento
            existencias[indice_paralelo] -= venta_herramienta
            print(f"\nSe a vendido {herramientas[indice_paralelo]} por {venta_herramienta} unidades")
            input("\nPresione una tecla, para volver al menú.")

        elif actualizacion == 2:
             print("\nIngreso de stock - Seleccione herramienta:")
             print("-"*30)
             for i in range (len(herramientas)):
                  print(f"{herramientas[i]} - Stock: {existencias[i]}")
             
             while True:
                seleccion_herramienta = input("-> ").strip()
                if not seleccion_herramienta.isalpha():
                    print("Error: Solo se aceptan letras")
                    continue
                if not seleccion_herramienta in herramientas:
                     print("\nLa herramienta no se encuentra disponible en el catalogo, ingrese nuevamente\n")
                     continue
                break
             
             indice_paralelo = herramientas.index(seleccion_herramienta)
             
             while True:
                aumentar_stock = input("Ingrese cantidad a agregar al stock: ")
                if not aumentar_stock.lstrip("-").isdigit():
                     print("Error: Solo se aceptan números")
                     continue
                aumentar_stock = int(aumentar_stock)

                # No se permite agregar una cantidad menor o igual a 0
                if aumentar_stock <= 0:
                    print("Error: El ingreso de stock debe ser mayor a 0\nNo se aceptan números negativos")
                    continue
                break
             # Utilizando el indice dentro de la lista existencias,
             # se le suma y reasigna el numero ingresado a este elemento
             existencias[indice_paralelo] += aumentar_stock
             print("Cantidad agregada correctamente")
             
        elif actualizacion == 3:
             continue

    elif opcion == 8: # Salir
        # Termina la ejecución del programa
        print("Sistema Cerrado")

    else:
        print("-"*65)
        print("Error: Opción inválida\n"\
                "Seleccione una opción del menú")

