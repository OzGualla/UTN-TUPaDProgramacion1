
# Declaración de listas a utilizar, que compartirán índice 
# para asociar cada herramienta con su cantidad de stock
herramientas = []
existencias = []
# Declaración de variables a utilizar
cantidad_herramientas = ""
cantidad_existencias = ""
opcion = ""

# Menú iterativo, se repite hasta que el usuario seleccione la opción de salir (8)
while True:
    # Vista del menú iterativo
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

            # El programa no acepta numeros negativos
            cantidad_herramientas = input("\nIngrese cantidad de herramientas a registrar: ")
            while cantidad_herramientas.startswith("-"):
                        print("\nError: No se aceptan números negativos")
                        cantidad_herramientas = input("Ingrese cantidad de herramientas a registrar: ")

            # Solo se aceptan números a excepción del 0 ya que no se puede registrar 0 herramientas.
            while not cantidad_herramientas.isdigit() or cantidad_herramientas == "0":
                print("Ingrese numero válido")
                cantidad_herramientas = input("\nIngrese cantidad de herramientas a registrar: ")

            cantidad_herramientas = int(cantidad_herramientas)

            # Una vez declarada la cantidad de iteraciones, se pide el ingreso de herramientas
            for i in range(cantidad_herramientas):
                herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip()
                # Verificación, solo se aceptan letras y no se aceptan espacios
                while not herramienta_ingresada.isalpha():
                    print("nombre no válido, solo se aceptan letras")
                    herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip()

                # Si el input ya se encuentra dentro de la lista, no se acepta el ingreso
                while herramienta_ingresada in herramientas:
                    print("Error: Herramienta ya ingresada\n"\
                        "Ingrese otra herramienta")
                    herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip()
                    # Verificación, solo se aceptan letras y no se aceptan espacios
                    while not herramienta_ingresada.isalpha():
                        print("nombre no válido, solo se aceptan letras")
                        herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ").strip()
                
                herramientas.append(herramienta_ingresada)

        elif opcion == 2: # Carga de Existencias
            # Si la lista herramientas se encuentra vacía, te devuelve al menú principal
            if herramientas == []:
                    print("-"*65)
                    print("\nError: Aún no se registraron herramientas:\n"\
                          "Por favor, primero registre herramientas.")
                    break

            for i in range(cantidad_herramientas):
                print("\n--- Carga de Existencias ---")
                cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                    f"para la herramienta: {herramientas[i]} -> ")
                # Verificación, Si el número es negativo, se vuelve a pedir el ingreso
                while cantidad_existencias.startswith("-"):
                        print("\nError: No se aceptan números negativos")
                        cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                        f"para la herramienta: {herramientas[i]} -> ")
                # por otro lado, si el ingreso no es un número, también se vuelve a pedir el ingreso
                while not cantidad_existencias.isdigit():
                        print("\nError: Solo se aceptan números")
                        cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                        f"para la herramienta: {herramientas[i]} -> ")
                # Si el ingreso es válido, se agrega la cantidad de existencias al final de la lista en cada iteración
                # Asegurando que se comparte el índice con la lista herramientas,
                cantidad_existencias = int(cantidad_existencias)
                existencias.append(cantidad_existencias)
                # Con cada ingreso, se muestra la herramienta junto a su stock asociado
                print(f"\n{herramientas[i]}: {existencias[i]} unidades")

        elif opcion == 3: # Visualización de Inventario
            # Si no se registraron herramientas, vuelve al menú
            if herramientas == []:
                print("\nInventario vacío. por favor Registre herramientas")
                break
            # Si se registraron herramientas pero no se ingresaron existencias
            # al momento de seleccionar esta opción, vuelve al menú mostrando el error correspondiente
            if existencias == []:
                print("\nError: herramientas sin stock disponible\n"\
                       "Por favor, primero asigne stock a las herramientas")
                break

            print("\n--- Inventario Actual ---\n"\
                  "-----------------------")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]} unidades")

            # Este input es solo para poder visualizar el inventario, 
            # Sin que la vista del menú iterable moleste al usuario
            input("Presione una tecla, para volver al menú.")

        elif opcion == 4: # Consulta de Stock
            print("--- Consulta de Stock ---")
            buscar_herramienta = input("Ingrese el nombre de la herramienta que quiera consultar: ")
            # Si el nombre ingresado coincide con la lista
            if buscar_herramienta in herramientas:
                # Se guarda el índice asociado
                herramienta_encontrada = herramientas.index(buscar_herramienta)
                # Y se utiliza esta variable para recorrer la lista paralela y asociar el indice con la cantidad de stock
                print(f"\n{buscar_herramienta.capitalize()}, Stock actual: {existencias[herramienta_encontrada]}")
                input("Presione una tecla, para volver al menú.")

        elif opcion == 5: # Reporte de Agotados
            print("--- Reporte de Agotados ---")

            for i in range(len(existencias)):
                if existencias[i] == 0:
                    # Lo imprime por pantalla junto al elemento asociado en la lista paralela
                    # de esta forma logrando visualizar solo las herramientas con stock 0
                    print(f"{herramientas[i]}: {existencias[i]} unidades")

        elif opcion == 6: # Alta de Nuevo Producto
            print("--- Alta de nuevo producto ---")
            # Se permite ingresar un nuevo elemento a la lista herramientas
            nueva_herramienta = input("Ingrese nombre de nueva herramienta: ").strip()
            # Si este elemento ya se encuentra, se vuelve al menú de opciones
            # Mostrando el error correspondiente
            if nueva_herramienta in herramientas:
                print("\nError: La herramienta ya se encuentra en Stock")
                break
            # Sucede lo mismo si el elemento no se encuentra en la lista
            # Pero este no es una letra
            if not nueva_herramienta.isalpha():
                print("Error: No se ha ingresado ningún nombre de herramienta")
                break
            # Luego se pide cantidad de stock
            nueva_existencia = input(f"Ingrese stock de {nueva_herramienta.capitalize()}")
            # Si no es un número, se vuelve al menú de opciones
            # Mostrando el error correspondiente
            if nueva_existencia.isalpha():
                print("Error: No se ha ingresado un número")
                break

            nueva_existencia = int(nueva_existencia)

            if nueva_existencia < 0:
                # Si nueva_existencia es menor a 0, se vuelve al menú de opciones
                # Mostrando el error correspondiente
                print("Error: No se puede agregar una cantidad menor a 0")
                break
            # Por último se agregan los elementos a sus listas e índices correspondientes
            # Asegurando de esta forma, que compartirán índice
            herramientas.append(nueva_herramienta)
            existencias.append(nueva_existencia)
        
        elif opcion == 7: # Actualizacion de Stock
            print("--- Actualizacion de Stock ---")

            if herramientas == []:
                 print("-"*65)
                 print("\nError: Aún no se registraron herramientas:\n"\
                       "Por favor, primero registre herramientas.")
                 break
            
            if existencias == []:
                 print("-"*65)
                 print("\nError: herramientas sin stock disponible\n"\
                       "Por favor, primero asigne stock a las herramientas")
                 break
            
            actualizacion = input("1 - Ventas\n2 - Ingreso\n3 - Volver\n-> ")

            while not actualizacion.isdigit():
                print("Error: Solo se aceptan numeros")
                actualizacion = input("1 - Ventas\n2 - Ingreso\n-> ")
            actualizacion = int(actualizacion)

            if actualizacion == 1:
                print("\nVenta - Seleccione herramienta:")
                for i in range(len(herramientas)):
                    print(f"{herramientas[i]} - Stock: {existencias[i]}")
                venta = input("-> ").strip()

                while not venta.isalpha():
                        print("Error: Solo se aceptan letras")
                        venta = input("-> ").strip()
                while venta not in herramientas:
                        for i in herramientas:
                             print(i)
                        print("La herramienta no se encuentra disponible en el catalogo, ingrese nuevamente")
                        venta = input("-> ").strip()
                print("nono trolo")
            
            elif actualizacion == 2:
                pass

            elif actualizacion == 3:
                break

            else:
                print("Opcion invalida")
            if venta in herramientas:
                print(venta)
            
            pass

        elif opcion == 8: # Salir
            # Termina la ejecución del programa
            print("Sistema Cerrado")
            break

        # En caso de ingresar un número que no se encuentra dentro de las opciones del menú, se muestra el error correspondiente
        else:
            print("-"*65)
            print("Error: Opción inválida\n"\
                  "Seleccione una opción del menú")