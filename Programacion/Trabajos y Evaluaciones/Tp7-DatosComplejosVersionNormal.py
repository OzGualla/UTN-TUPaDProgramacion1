""" Tp7 - Estructuras de datos complejas """

# -----------------------
# definición de funciones
# -----------------------

# Funciones que cree, ajenas al trabaja practico, para validar isalpha() o isdigit()

def validar_letras(palabra):
    """
    Si el parámetro no es alfabético
    no acepta la entrada y vuelve a pedir el input
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
    Si el parámetro no es un dígito
    no acepta la entrada y vuelve a pedir el input
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

# -------------------------------------------------------
# Programa principal
# -------------------------------------------------------

# -----------------------
# Ejercicio 1:          
# -----------------------
# Se crea el diccionario:
precios_frutas = {
    "Banana":1200,
    "Ananá":2500,
    "Melón":3000,
    "Uva":1450
}
# Con el método .update se agregan varias claves\valor al diccionario declarado
precios_frutas.update({"Naranja":1200,"Manzana":1500,"Pera":2300})

print(f"\nEjercicio 1: {precios_frutas}\n")

# -----------------------
# Ejercicio 2:
# -----------------------
# Se reasignan los valores a las claves
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"\nEjercicio 2: {precios_frutas}\n")

# -----------------------
# Ejercicio 3:
# -----------------------
# Se crea una lista, con los claves del diccionario declarado
lista_de_precios = precios_frutas.keys()
lista_de_precios = list(lista_de_precios)

print(f"\nEjercicio 3: {lista_de_precios}\n")

ejercicio_siguiente()

# -----------------------
# Ejercicio 4:
# -----------------------
# Permite almacenar nombres y números telefónicos
print("\nEjercicio 4:")

contactos = {}
# Se pide ingresar el nombre de 5 contactos, los que se asignaran como claves
for i in range(5):
    nombre = validar_letras(input(f"\nIngrese el nombre del contacto n° {i+1}/5: "))
    # si el contacto ya se encuentra en la lista, no acepta la entrada
    while nombre in contactos:
        print(f"\n{nombre.capitalize()} ya se encuentra en sus contactos")
        nombre = validar_letras(input(f"Ingrese el nombre del contacto n° {i+1}/5: "))
        continue
    # Pide asignar un numero para el contacto
    telefono = validar_numeros(input(f"\nIngrese el número de teléfono del contacto {nombre.capitalize()}: "))
    # y se le asigna la entrada como valor
    contactos[nombre] = telefono

print(contactos)

buscar_contacto = ""

while True:
    buscar_contacto = validar_letras(input("\nBuscar contacto: ").lower())
    print("(Ingrese 'salir' para terminar)")

    if buscar_contacto == "salir":
        break
    # Si la clave del contacto esta en el dict muestra su numero asociado como valor
    if buscar_contacto in contactos:
        print(f"=== Numero de {buscar_contacto}: {contactos[buscar_contacto]} ===")
        continue
    # Si no se encuentra, muestra un mensaje
    else:
        print("=== Contacto no agendado ===")
        continue

# Ejercicio 5

# En este ejercicio no se valida la entrada, se aceptan " " caracteres especiales y dígitos
frase = input("\nIngrese una frase: ").lower()
recuento = {}

# Usando la función .split creo una nueva lista, con las palabras de la frase ingresada
palabras = frase.split()
# Convierto la lista en un set para eliminar los duplicados
palabras_unicas = set(palabras)
# Y muestro las palabras únicas de la frase por pantalla
print(f"Palabras únicas: {palabras_unicas}")

# Utilizo el .get saber las ocurrencias, se inicializa en 0
# y le sumo +1 cada vez que aparece en la lista
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
# Y muestro la cantidad de veces que aparece cada palabra
print(recuento)

ejercicio_siguiente()

# -----------------------
# Ejercicio 6:
# -----------------------
# Permite ingresar 3 nombres, con 3 notas y luego muestra el promedio para cada alumno correspondiente
print("\nEjercicio 6:")

alumnos = {}
sumatoria = ""

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

print()

for nombre, notas in alumnos.items():
    # con la función sum() sumo los elementos de la tupla
    # con la función len() se consigue la cantidad de elementos, por la que se dividirá la suma
    promedio = sum(notas) / len(notas)

    print(f"El promedio del alumno {nombre} es: {promedio:.2f}")

ejercicio_siguiente()

# -----------------------
# Ejercicio 7:
# -----------------------
# Muestra la cantidad de asistencias a una capacitación por persona
print("\nEjercicio 7:")

asistencias = ["Ana", "Yuliana", "Luis", "Ana", "Yuliana","Maria", "Luis", "Pedro", "Ana", "Yuliana","Yuliana",]

print(f"\nLista original: {asistencias}")

# Genero un conjunto, para eliminar los repetidos
asistencias_por_persona = set(asistencias)

print(f"\nEmpleados que asistieron a la capacitación:\n{asistencias_por_persona}")

print("\nAsistencias por empleado:")
# Recorro el conjunto con un for
# Pero obtengo el valor .count de la lista para saber la cantidad de repetidos
for nombre in asistencias_por_persona:
    print(f"{nombre}: {asistencias.count(nombre)}")   

ejercicio_siguiente()

# -----------------------
# Ejercicio 8:
# -----------------------
# Agregar stock y nuevos productos a diccionario
print("\nEjercicio 8:")

productos = {
    "harina": 10,
    "leche": 5,
    "arroz": 7,
    "manteca": 2,
    "fideos": 10,
    "huevos": 12,
}

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
    elif consulta_stock in productos.keys():
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

ejercicio_siguiente()

# -----------------------
# Ejercicio 9:
# -----------------------
# Agenda con eventos, por dia y horario
print("\nEjercicio 9:")

# Dict donde las claves, son una tupla (dia, hora) y los valores eventos
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes","15:00"): "Clase de inglés",
    ("miercoles","14:00"): "Clase de natación",
    ("jueves","18:00"): "Clase de programación",
    ("viernes","12:00"): "Almuerzo Familiar",
}

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
        print("\nTenes: ", evento)
        continue
    # Si no existe, muestra mensaje, pero no tira error 
    # gracias al .get()
    else:
        print("\nNo hay actividades en ese horario")
        continue
print("\n=== Agenda finalizada ===")

ejercicio_siguiente()


# -----------------------
# Ejercicio 10:
# -----------------------
# Invertir clave-valor en diccionario
print("\nEjercicio 10:")

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brazil": "Brasilia",
    "Peru": "Lima",
    "Uruguay": "Montevideo",
    "Ecuador": "Quito"
}

invertido = {}

# Se recorre tanto calve, como valor
for clave, valor in original.items():
    # Y se asignan en orden invertido, en un nuevo diccionario  
    invertido[valor] = clave

# Luego se muestran ambos por pantalla
print(f"\nDiccionario original:\n{original}\n")
print(f"Diccionario invertido:\n{invertido}\n")

print("=== Gracias por su tiempo! ===")
