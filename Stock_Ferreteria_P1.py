
# Declaracion de listas
herramientas = []
existencias = []
# Declaracion de variables
cantidad_herramientas = ""
cantidad_existencias = ""
opcion = ""

while True:
    # Menu iterativo
    while opcion != "8":
        print("-"*65)
        print("\n---- Sistema de Stock ----")
        print("\n1 - Carga inicial de Herramientas\n"\
            "2 - Carga de Existencias\n"\
            "3 - Visualizacion de Inventario\n"\
            "4 - Consulta de Stock\n"\
            "5 - Reporte de Agotados\n"\
            "6 - Alta de Nuevo Producto\n"\
            "7 - Actualizacion de Stock\n"\
            "8 - Salir")
        opcion = input("-> ")
        # Verificacion de menu, solo se aceptan numeros
        # Vuelvo a mostrar el menu, solo para evitar scrolear para volver a ver las opciones
        # En caso de ingresar varias entradas invalidas
        while not opcion.isdigit():
            print("-"*65)
            print("\nOpcion invalida\nSolo se aceptan numeros")
            print("\n\n---- Sistema de Stock ----")
            print("\n1 - Carga inicial de Herramientas\n"\
            "2 - Carga de Existencias\n"\
            "3 - Visualizacion de Inventario\n"\
            "4 - Consulta de Stock\n"\
            "5 - Reporte de Agotados\n"\
            "6 - Alta de Nuevo Producto\n"\
            "7 - Actualizacion de Stock\n"\
            "8 - Salir")
            opcion = input("-> ")
        
        # Seleccion de menu
        if opcion == "1": # Carga inicial de Herramientas
            print("\n--- Carga de herramientas ---")
            cantidad_herramientas = input("\nIngrese cantidad de herramientas a registrar: ")

            # Solo se aceptan numeros a excepcion del 0
            while not cantidad_herramientas.isdigit() or cantidad_herramientas == "0":
                print("Ingrese numero valido")
                cantidad_herramientas = input("\nIngrese cantidad de herramientas a registrar: ")

            # Conversion del tipo de dato de entrada
            cantidad_herramientas = int(cantidad_herramientas)

            # Una vez declarada la cantidad de iteraciones, se pide el ingreso de estas
            for i in range(cantidad_herramientas):
                herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ")
                # Verificacion, solo se aceptan letras
                while not herramienta_ingresada.isalpha():
                    print("nombre no valido, solo se aceptan letras")
                    herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ")

                # Si el input ya se encuentra dentro de la lista, no se acepta el ingreso
                while herramienta_ingresada in herramientas:
                    print("Error: Herramienta ya ingresada\n"\
                        "Intente denuevo")
                    herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ")
                    # Verificacion, solo se aceptan letras
                    while not herramienta_ingresada.isalpha():
                        print("nombre no valido, solo se aceptan letras")
                        herramienta_ingresada = input(f"\nIngrese nombre de herramienta n°{i+1}/{cantidad_herramientas}: ")
                
                # Ingreso de elementos en la lista
                herramientas.append(herramienta_ingresada)

        elif opcion == "2": # Carga de Existencias
            # Si la lista herramientas se encuentra vacia, te devuelve al menu principal
            if herramientas == []:
                    print("-"*65)
                    print("\nError: Aun no se registraron Herramientas:\n"\
                          "Por favor, primero registre herramientas.")
                    break
            # Usando la variable ya ingresada, se recorre este for un numero igual de veces
            # Al ingreso de herramientas
            for i in range(cantidad_herramientas):
                print("\n--- Carga de Existencias ---")
                cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                    f"para la herramienta: {herramientas[i]} -> ")
                # Verificacion, Si el numero es negativo, se vuelve a pedir el ingreso
                while True:
                    if cantidad_existencias.startswith("-"):
                        print("\nError: No se aceptan numeros negativos")
                        cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                        f"para la herramienta: {herramientas[i]} -> ")
                # por otro lado, si el ingreso no es un numero, tambien se vuelve a pedir el ingreso
                    elif not cantidad_existencias.isdigit():
                        print("\nError: Solo se aceptan numeros")
                        cantidad_existencias = input("Ingrese la cantidad de unidades\n"\
                        f"para la herramienta: {herramientas[i]} -> ")
            # De ser valido, se ingresa la cantidad de existencias a la lista existencias
            # Compartiendo indice con la lista herramientas
            # Conversion de tipo de dato de entrada  
            cantidad_existencias = int(cantidad_existencias)
            existencias.append(cantidad_existencias)
            print(f"\n{herramientas[i]}: {existencias[i]} unidades")
        
        elif opcion == "3": # Visualizacion de Inventario
            # Si no se registraron herramientas, vuelve al menu
            if herramientas == []:
                print("\nInventario vacio. por favor Registre herramientas")
                break
            # Si se registraron herramientas pero no se ingresaron existencias
            # al momento de selecionar esta opcion, vuelve al menu mostrando el error correspondiente
            if existencias == []:
                print("\nHerramientas registradas sin cantidad\n"\
                      "Por favor ingrese cantidad de existencias.")
                break
            # Muestro ambas listas ordenadas por indice
            print("\n--- Inventario Actual ---\n"\
                  "-----------------------")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]} unidades")
            # Este imput es solo para poder visualizar el inventario , 
            # Sin que la vista del menu iterable moleste al usuario
            input("Precione una tacla, para volver al menu.")
        
        elif opcion == "4": # Consulta de Stock
            print("--- Consulta de Stock ---")
            buscar_herramienta = input("Ingrese el nombre de la herramienta que quiera consultar: ")
            # Si el nombre ingresado coincide con la lista
            if buscar_herramienta in herramientas:
                # Se guarda el indice asociado
                herramienta_encontrada = herramientas.index(buscar_herramienta)
                # Y se utiliza para recorrer la lista paralela
                print(f"\n{buscar_herramienta.capitalize()}, Stock acutal: {existencias[herramienta_encontrada]}")
                input("Precione una tecla, para volver al menu.")
        
        elif opcion == "5": # Reporte de Agotados
            print("--- Reporte de Agotados ---")
            # utilizando el tamaño de la lista existencias
            for i in range(len(existencias)):
                # recorro dicha lista por indice
                # Si el elemento es igual a 0
                if existencias[i] == 0:
                    # Lo imprime por pantalla junto al elemento asociado en la lista paralela
                    print(f"{herramientas[i]}: {existencias[i]} unidades")

        elif opcion == "6": # Alta de Nuevo Producto
            print("--- Alta de nuevo producto ---")
            # Se permite ingresar un nuevo elemento a la lista herramientas
            nueva_herramienta = input("Ingrese nombre de nueva herramienta: ")
            # Si este elemento ya se encuentra, se vuelve al menu de opciones
            # Mostrando el error correspondiente
            if nueva_herramienta in herramientas:
                print("\nError: La herramienta ya se encuentra en Stock")
                break
            # Sucede lo mismo si el elemento no se encuentra en la lista
            # Pero este no es una letra
            if not nueva_herramienta.isalpha():
                print("Error: No se ha ingresado ningun nombre de herramienta")
                break
            # Luego se pide cantidad de Stock
            nueva_existencia = input(f"Ingrese Stock de {nueva_herramienta.capitalize()}")
            # Si no es un numero, se vuelve al menu de opciones
            # Mostrando el error correspondiente
            if nueva_existencia.isalpha():
                print("Error: No se ha ingresado un numero")
                break
            # Conversion de tipo de dato de entrada
            nueva_existencia = int(nueva_existencia)
            # Ahora verifica si el numero es menor a 0
            if nueva_existencia < 0:
                # Si lo es, se vuelve al menu de opciones
                # Mostrando el error correspondiente
                print("Error: No se puede agregar una cantidad menor a 0")
                break
            # Por ultimo se agregan los elementos a sus listas e indices correspondientes
            # Asegurando de esta forma, que compartiran indice
            herramientas.append(nueva_herramienta)
            existencias.append(nueva_existencia)
        
        elif opcion == "7":
            pass

        elif opcion == "8": # Salir
            print("Sistema Cerrado")
            break
        else:
            print("\nOpcion invalida")    