
""" Tp7 - Estructuras de datos complejas """

# =======================
# definición de funciones
# =======================

# Funciones que cree, ajenas al trabaja practico, para validar isalpha() o isdigit()

def validar_letras(palabra):
    """
    Recibe como parámetro:
    palabra (str)
    Y retorna:
    palabra (str) validado
    """
    while not palabra.isalpha():
        print("\nSolo se aceptan letras")
        palabra = input("Ingrese nuevamente: ")
    return palabra

def validar_numeros(numero):
    """
    Recibe como parámetro:
    numero (str)
    Y retorna:
    numero (int) validado
    """
    while not numero.isdigit():
        print("\nSolo se aceptan números positivos")
        numero = input("Ingrese nuevamente: ")
    numero = int(numero)
    return numero

def ejercicio_siguiente():
    """ Realiza una pausa, hasta que el usuario ingrese una tecla """
    input("Presione una tecla para continuar. ")

# ============
# Ejercicio 1:          
# ============

def trabajar_precios():
    """ Ejercicio 1,2 y 3 
        agrega elementos al dict
        modifica sus valores"""
    precios_frutas = {
        "Banana":1200,
        "Ananá":2500,
        "Melón":3000,
        "Uva":1450
    }

    # Con el método .update se agregan varias claves\valor al diccionario declarado
    precios_frutas.update({"Naranja":1200,"Manzana":1500,"Pera":2300})

    print(f"\nEjercicio 1: {precios_frutas}\n")

    # ============
    # Ejercicio 2:
    # ============
    # Se reasignan los valores a las claves
    precios_frutas["Banana"] = 1330
    precios_frutas["Manzana"] = 1700
    precios_frutas["Melón"] = 2800

    print(f"\nEjercicio 2: {precios_frutas}\n")

    # ============
    # Ejercicio 3:
    # ============
    # Se crea una lista, con los claves del diccionario declarado
    lista_de_precios = precios_frutas.keys()
    lista_de_precios = list(lista_de_precios)

    print(f"\nEjercicio 3: {lista_de_precios}\n")

# ============
# Ejercicio 4:
# ============

def agregar_contactos():
    """ Registra 5 contactos
        y agrega un numero telefónico para c/u"""
    contactos = {}
    # Se pide ingresar el nombre de 5 contactos, los que se asignaran como claves
    for i in range(5):
        nombre = validar_letras(input(f"\nIngrese el nombre del contacto n° {i+1}/5: ").lower())
        # si el contacto ya se encuentra en la lista, no acepta la entrada
        while nombre in contactos:
            print(f"\n{nombre.capitalize()} ya se encuentra en sus contactos")
            nombre = validar_letras(input(f"Ingrese el nombre del contacto n° {i+1}/5: ").lower())
            continue
        # Pide asignar un numero para el contacto
        telefono = validar_numeros(input(f"\nIngrese el número de teléfono del contacto {nombre.capitalize()}: "))
        # y se le asigna la entrada como valor
        contactos[nombre] = telefono
    return contactos

def buscar_contacto(contactos):
    """ Busca el contacto en el dict
        y devuelve su valor si lo encuentra"""
    buscar_nombre = ""

    while True:
        buscar_nombre = validar_letras(input("\nBuscar contacto: ").lower())
        print("(Ingrese 'salir' para terminar)")

        if buscar_nombre == "salir":
            break
        # Si la clave del contacto esta en el dict muestra su numero asociado como valor
        if buscar_nombre in contactos:
            print(f"=== Numero de {buscar_nombre.capitalize()}: {contactos[buscar_nombre]} ===")
            continue
        # Si no se encuentra, muestra un mensaje
        else:
            print("=== Contacto no agendado ===")
            continue

# ============
# Ejercicio 5:
# ============

def separar_frase(frase):
    """ Separa una frase en palabras
        Y suma las ocurrencias """
    recuento = {}
    # Usando la función .split creo una nueva lista.
    palabras = frase.split()
    # Convierto la lista en un set para eliminar los duplicados
    palabras_unicas = set(palabras)
    # Utilizo el .get para contar ocurrencias (con valor 0 inicial) 
    # y le sumo +1 cada vez que aparece en la lista
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1
    # Retorno un set con las palabras
    # y la cantidad ocurrencias
    return palabras_unicas, recuento

# ============
# Ejercicio 6:
# ============

def ingresar_alumno_y_nota():
    """ Registra el nombre de 3 alumnos
        Y 3 notas para cada uno """
    
    alumnos = {}

    for alumno in range(3):
        nombre_alumno = validar_letras(input(f"\nIngrese el nombre del alumno {alumno+1}/3: ").capitalize())
        # Si se detecta que el nombre ya existe dentro del diccionario, se vuelve a pedir el ingreso.
        while nombre_alumno in alumnos:
            print("\nEl alumno ya se ha ingresado")
            nombre_alumno = validar_letras(input(f"Ingrese el nombre del alumno {alumno+1}/3: ").capitalize())
        
        # La lista vuelve a estar vacía en cada iteración
        notas = []

        for nota in range(3):
            nota_alumno = validar_numeros(input(f"Ingrese la nota {nota+1}/3: "))
            # Se agrega el elemento a la lista
            notas.append(nota_alumno)

        # y se crea una nueva tupla una vez ingresadas todas las entradas
        tupla_de_notas = tuple(notas)
        # Luego se le asigna la tupla, como valor a la clave ingresada
        alumnos[nombre_alumno] = tupla_de_notas
    return alumnos

def resultado(alumnos):
    """ Calcula el promedio """

    promedio = ""
    for nombre, notas in alumnos.items():
        # con la función sum() sumo los elementos de la tupla
        # con la función len() se consigue la cantidad de elementos, por la que se dividirá la suma
        promedio += f"El promedio del alumno {nombre} es: {(sum(notas) / len(notas)):.2f}\n"
    return promedio

# ============
# Ejercicio 7:
# ============

def contar_asistencias(lista):
    """Muestra la cantidad de asistencias a una capacitación por persona"""

    # Genero un conjunto, para eliminar los repetidos
    asistencias_por_persona = set(lista)
    mostrar_asistencias = ""
    # Recorro el conjunto para obtener los elementos.
    # Pero obtengo el valor .count() de la lista para saber la cantidad de repetidos
    for nombre in asistencias_por_persona:
        mostrar_asistencias += f"{nombre}: {lista.count(nombre)}\n"

    return asistencias_por_persona , mostrar_asistencias

# ============
# Ejercicio 8:
# ============

def productos_stock(productos):
    """ Permite agregar mas productos al diccionario
        y modificar stock de los existentes"""
    
    consulta_stock = ""

    while True:
        print("=== Consulta de Stock ===")
        # Recorro el dict para una clara visualización de productos
        for producto in productos.keys():
            print(f"- {producto}")

        print("(Ingrese 'salir' para terminar)")

        consulta_stock = validar_letras(input("\nElija producto:\n-> "))
        # El programa iterara hasta que se cumpla la condición
        if consulta_stock.lower() == "salir":
            break

        # Si la clave existe dentro del dict    
        if consulta_stock in productos.keys():
            # Se muestra su valor
            print(f"\nStock disponible: {productos[consulta_stock]}")
            print("\n=== Agregar stock ===")
            agregar_stock = validar_numeros(input("Seleccione cantidad: "))
            # Y se le agrega la cantidad deseada
            productos[consulta_stock] += agregar_stock
            # y vuelve al menu

        # Si la clave no existe, la agrega como nuevo producto
        else:
            print("\nProducto inexistente")
            print(f"Nuevo producto agregado: {consulta_stock}")
            # Se le asigna un stock
            agregar_stock=  validar_numeros(input("Seleccione cantidad de Stock de nuevo producto: "))
            productos[consulta_stock] = agregar_stock
            # y vuelve al menu

# ============
# Ejercicio 9:
# ============

def agenda_semanal(agenda):
    """ Muestra una agenda con eventos, por dia y horario """
    while True:
        print("\n=== Agenda actualizada ===")
        print("(Ingrese 'salir' para terminar)")
        # Se permite ingresar un dia
        dia = validar_letras(input("\nIngrese el día: "))

        if dia.lower() == "salir":
            break

        # Y un horario
        hora = input("Ingrese la hora: ")
        # Se itera el programa hasta cumplir la condición
        if hora.lower() == "salir":
            break
        # Utilizando .get() retorno el valor de la clave 
        evento = agenda.get((dia,hora))
        # si existe, se muestra por pantalla
        if evento:
            print("-"*30)
            print("\nTenes: ", evento)
            print("-"*30)
            continue
        # Si no existe, muestra mensaje, pero no tira error 
        # gracias al .get()
        else:
            print("\nNo hay actividades en ese horario")
            continue

# =============
# Ejercicio 10:
# =============

def invertir_clave_valor(diccionario):
    """Invierte clave-valor del diccionario"""
    invertido = {}

    # Se recorre tanto calve, como valor
    for clave, valor in diccionario.items():
        # Y se asignan en orden invertido, en un nuevo diccionario  
        invertido[valor] = clave
    return invertido

# ====================
# Estructura principal
# ====================

# Opte por utilizar Match Case, por prolijidad y organización
while True:
    print("\n=== Menú ===")
    print("1 - Ejercicio 1, 2 y 3")
    print("2 - Ejercicio 4")
    print("3 - Ejercicio 5")
    print("4 - Ejercicio 6")
    print("5 - Ejercicio 7")
    print("6 - Ejercicio 8")
    print("7 - Ejercicio 9")
    print("8 - Ejercicio 10")
    print("0 - Salir")
    opcion = validar_numeros(input("Seleccione Ejercicio: "))

    match opcion:
        case 1:    
            # ==================
            # Ejercicio 1, 2 y 3:
            # ==================
            trabajar_precios()

            ejercicio_siguiente()

        case 2:
            # ============
            # Ejercicio 4:
            # ============
            print("-"*65)
            print("\nEjercicio 4:")

            diccionario_contactos = agregar_contactos()
            buscar_contacto(diccionario_contactos)

            ejercicio_siguiente()

        case 3:
            # ============
            # Ejercicio 5:
            # ============
            print("-"*65)
            print("\nEjercicio 5:")

            palabras_unicas, recuento = separar_frase(frase = input("Ingrese una frase: ").lower())

            print(f"Palabras únicas: {palabras_unicas}")
            print(recuento)

            ejercicio_siguiente()

        case 4:
            # ============
            # Ejercicio 6:
            # ============
            print("-"*65)
            print("\nEjercicio 6:")

            diccionario_alumnos = ingresar_alumno_y_nota()
            promedio_alumnos = resultado(diccionario_alumnos)
            print(promedio_alumnos)

            ejercicio_siguiente()

        case 5:
            # ============
            # Ejercicio 7:
            # ============
            print("-"*65)
            print("\nEjercicio 7:")

            asistencias = ["Ana", "Yuliana", "Luis", "Ana", "Yuliana","Maria", "Luis", "Pedro", "Ana", "Yuliana","Yuliana",]

            print(f"\nLista original: {asistencias}")

            asistencias_por_persona, mostrar_asistencias = contar_asistencias(asistencias)

            print(f"\nEmpleados que asistieron a la capacitación: {asistencias_por_persona}")
            print("\nAsistencias por empleado:")

            print(f"{mostrar_asistencias}")

            ejercicio_siguiente()

        case 6:
            # ============
            # Ejercicio 8:
            # ============
            print("-"*65)
            print("\nEjercicio 8:")

            productos = {
                "harina": 10,
                "leche": 5,
                "arroz": 7,
                "manteca": 2,
                "fideos": 10,
                "huevos": 12,
            }

            productos_stock(productos)

            ejercicio_siguiente()

        case 7:
            # ============
            # Ejercicio 9:
            # ============
            print("-"*65)
            print("\nEjercicio 9:")

            # Dict donde las claves, son una tupla (dia, hora) y los valores eventos
            agenda = {
                ("lunes", "10:00"): "Reunión",
                ("martes","15:00"): "Clase de inglés",
                ("miercoles","14:00"): "Clase de natación",
                ("jueves","18:00"): "Clase de programación",
                ("viernes","12:00"): "Almuerzo Familiar",
            }

            agenda_semanal(agenda)
            print("\n=== Agenda finalizada ===")

            ejercicio_siguiente()

        case 8:
            # =============
            # Ejercicio 10:
            # =============
            print("-"*65)
            print("\nEjercicio 10:")

            # Declaro diccionario a invertir
            dict_original = {
                "Argentina": "Buenos Aires",
                "Chile": "Santiago",
                "Brazil": "Brasilia",
                "Peru": "Lima",
                "Uruguay": "Montevideo",
                "Ecuador": "Quito"
            }

            dict_invertido = invertir_clave_valor(dict_original)

            print(f"\nDiccionario original:\n{dict_original}\n")
            print(f"Diccionario invertido:\n{dict_invertido}\n")

            ejercicio_siguiente()
        
        case 0:
            print("=== Gracias por su tiempo! ===\n")
            break

        case _:
            print("=== Opción invalida ===")