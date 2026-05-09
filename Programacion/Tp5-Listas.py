""" Tp5- Listas"""
print("\n------- Bienvenido al TP5 - Listas -------\n")

# Ejercicio 1: Nota Alumno, promedio, mínimo y máximo

print("Ejercicio 1:\n")
print("Notas de alumnos:\n")
# Creo una lista anidada con las notas y los alumnos
notas = [["Aron",6.50],["Baro",10],["Dona",3.33],["Juan",4],["Zoey",8]]
suma_notas = 0
# Uso los valores mínimos y máximos de python
# Para encontrar los valores mínimos de las variables
nota_minima = float("inf")
nota_maxima = float("-inf")
pos_min = ""
pos_max = ""
print("Alumno   Nota")
print("-------------")
for alumno,nota in notas:
    # Muestra la lista completa
    print(f"{alumno}      {nota}")
    suma_notas += nota
    # Guarda la nota menor y el nombre del alumno
    if nota < nota_minima:
        nota_minima = nota
        pos_min = alumno
    # Guarda la nota mayor y el nombre del alumno
    if nota > nota_maxima:
        nota_maxima = nota
        pos_max = alumno
# Muestra Promedio en primera instancia
# Se dejo un espacio solo para que al imprimir por pantalla se vea prolijo
promedio = suma_notas /              len(notas)
# Muestra Menor y Mayor
print(f"\nLa nota menor es de {pos_min}: {nota_minima:.2f}")
print(f"La nota mayor es de {pos_max}: {nota_maxima:.2f}")
# Muestra Promedio en segunda instancia
print(f"El promedio de las notas es: {promedio:.2f}")
print("-"*65)
# decidí poner un input al final de cada ejercicio, para que
# la ejecución siguiente, no tape el resultado final del código actual
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 2 Ingreso y eliminación de productos

# Creo una lista vacía donde almacenar los elementos ingresados
print("\nEjercicio 2:")
print("Ingreso de 5 productos:\n")
productos = []
print("\n-- Bienvenido --")
# Declaro cuantas veces itera el for
for producto in range(5):
    # Se valida que el nombre no quede vació
    ingreso = input(f"Ingrese producto: ").strip()
    # Y que sean solo letras
    while not ingreso.isalpha():
        print("Error: Solo se aceptan letras")
        ingreso = input(f"Ingrese producto: ").strip()
    while ingreso in productos:
        print("El producto ya se encuentra en la lista")
        ingreso = input(f"Ingrese producto: ").strip()
    # y cada input es agregado a la lista, hasta llenar los 5 elementos
    productos.append(ingreso)
    # Acomodo la lista por orden alfabético
    productos.sort()
    # Muestro la lista
    print("productos ingresados:")
    for i in productos:
        print(i)

# Mientras la lista no este vacía, se repite preguntar si se eliminan elementos
while productos != []:
    opcion = input("Desea eliminar un producto? s/n -> ").strip()
    if opcion.lower() == "n":
    # Si decide que no desea eliminar ningún elemento termina la ejecución
        break
    # De requerir la eliminación de un producto
    elif opcion.lower() == "s":
        for i in productos:
            print(i)
        producto_eliminado = input("Producto a eliminar: ")
        # Si encuentra el elemento en la lista
        if producto_eliminado in productos:
            # Se consulta el indice de este
            producto_eliminado = productos.index(producto_eliminado)
            # Y se elimina
            productos.pop(producto_eliminado)
            # Se muestra la lista actualizada
            if productos != []:
                for i in productos:
                    print(i)
            else: # Si se eliminan todos los productos de la lista, se da aviso
                print("Su carrito se encuentra vació")
        else: # Si el input ingresa no coincide con un elemento dentro de la lista
            print("producto no hallado")
    else: # Validación por si se ingresa algo con no sea "s" o "n"
        print("Solo se aceptan letras")
print("Gracias, vuelva pronto!")
print("-"*65)
continuar = input("Presione una tecla para continuar: ")
#-----------------------------------------------------------------------------------------------------------

# Ejercicio 3: Separar Par e Impar

print("\nEjercicio 3: ")
print("Separar números pares e impares de una lista:\n")
import random
# Creo las listas vacías
numeros_enteros = []
numero_aleatorio = 0
lista_par = []
lista_impar = []
# Declaro un rango de 0 a 14
for numero in range(15):
    # Genero los números al azar
    numero_aleatorio = random.randint(1,100)
    # Ingreso los números aleatorios en la lista principal
    numeros_enteros.append(numero_aleatorio)
    # Separo par de impar en nuevas listas utilizando módulo
    if numero_aleatorio % 2 == 0:
        # Si el módulo es 0 las variables se agregan a lista_par
        lista_par.append(numero_aleatorio)
        lista_par.sort()
    if numero_aleatorio % 2 == 1:
        # Si el módulo es 1 las variables se agrega a lista_impar
        lista_impar.append(numero_aleatorio)
        lista_impar.sort()
# Imprimo resultado final, fuera del ciclo, para no llenar la pantalla por los print excesivos
print(numeros_enteros)
print(f"Números pares: {lista_par}")
print(f"Cantidad de números pares: {len(lista_par)}")
print(f"Números impares: {lista_impar}")
print(f"Cantidad de números impares: {len(lista_impar)}")  
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 4: Eliminar Repetidos de la lista y crear un nueva
print("\nEjercicio 4:")
# Creo la lista con repetidos y la nueva lista vacía
datos = [1,3,5,3,7,1,9,5,3]
lista_sin_repetidos = []
print("Eliminar repetidos de la lista y crear una nueva lista\n")
print(f"Lista original: {datos}")
# Recorre la lista, elemento por elemento
for dato in datos:
    # Si el dato ya existe en la nueva lista, ignora el ciclo
    if dato in lista_sin_repetidos:
        continue
    # Si el dato no existe en la nueva lista, lo agrega
    elif dato not in lista_sin_repetidos:
        lista_sin_repetidos.append(dato)
# Muestra el resultado
print(f"Nueva lista sin repetidos: {lista_sin_repetidos}")
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 5: Agregar y Eliminar estudiantes de lista
print("\nEjercicio 5:")
print("Agregar y eliminar estudiantes de lista\n")
# Declaro los elementos
estudiantes = ["Ivan","Demian","Juanito","Baro","Nadia","Malena","Andrea","Jessica"]

print("Estudiantes presentes:\n----------------------")
# Muestro los nombres de forma prolija
for estudiante in estudiantes:
    print(estudiante)

# Bucle simple para repetición 
# Mientras opción sea diferente a 3, se iterara
opcion = 0
while opcion != 3:
    # Solo un aviso al usuario si su lista se encuentra vacía
    # No modifica significativamente el código
    if estudiantes == []:
        print("No hay ningún estudiante presente")
    # Menú de opciones
    opcion = input("\n1 - Agregar estudiante\n2 - Eliminar estudiante\n3- Salir\n-> ")
    # Valida que la opción sea un dígito
    while not opcion.isdigit():
        print("\nError: Solo se aceptan números")
        print("Ingrese un número válido")
        opcion = input("\n1 - Agregar estudiante\n2 - Eliminar estudiante\n3- Salir\n-> ")
    # Conversión del tipo de dato de entrada
    opcion = int(opcion)
    
    # Agregar nombre a la lista
    if opcion == 1:
        # Se valida que el nombre no este vació
        nombre_estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").strip()
        # Y solo se aceptan letras
        while not nombre_estudiante.isalpha():
            print("Error: Solo se aceptan letras")
            nombre_estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").strip()
        # Si el nombre no esta en la lista estudiantes muestra el mensaje y vuelve a pedir el ingreso
        while nombre_estudiante.capitalize() in estudiantes:
            print("El estudiante ya se encuentra en la lista")
            nombre_estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").strip()
        # Se agrega el nuevo elemento al final de la lista estudiantes
        estudiantes.append(nombre_estudiante.capitalize())

    # Eliminar nombre de la lista
    elif opcion == 2:
        # Muestro la lista con los nombres, para que el usuario identifique los que quiere eliminar
        print()
        for estudiante in estudiantes:
            print(estudiante)
        # Se valida que el nombre no este vació
        nombre_estudiante = input("Ingrese el nombre del estudiante que desea eliminar: ").strip()
        # Y solo se aceptan letras
        while not nombre_estudiante.isalpha():
            print("Error: Solo se aceptan letras")
            nombre_estudiante = input("Ingrese el nombre del estudiante que desea eliminar: ").strip()
        # Si no encuentra el nombre, no elimina ningún elemento, solo se retoma el bucle inicial
        if nombre_estudiante.capitalize() not in estudiantes:
            print("\nNombre no válido")
            continue
        # Si encuentra el nombre dentro de la lista ,lo elimina
        estudiantes.remove(nombre_estudiante.capitalize())
    
    # Termina la ejecución del programa
    elif opcion == 3:
        break
    # Si ningún número corresponde a las opciones disponibles, muestra el error e itera el ciclo
    else:
        print("Error: Opción inválida")

# Finaliza mostrando la lista final
print()
for estudiante in estudiantes:
            print(estudiante)
print("-"*65)
continuar = input("Presioné una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 6: Rotar lista
print("\nEjercicio 6:")
print("\nRotar los elementos de la lista")

lista_a_rotar = [10, 20, 30, 40, 50, 60, 70]
print("\nLista original: ")

for i in lista_a_rotar:
    print(i, end=" ")
print()

guardar_ultimo_numero = lista_a_rotar.pop()
lista_a_rotar.insert(0, guardar_ultimo_numero)

print("\nLista rotada: ")
for i in lista_a_rotar:
    print(i, end=" ")
print()
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 7: Temperatura mínima y máxima
print("\nEjercicio 7:")
print("Temperatura mínima y máxima")
# Declaro la Matriz 7x2
temperatura = [[12,19],
               [10,18],
               [8,21],
               [21,27],
               [23,29],
               [19,25],
               [5,10]]
# Creo una lista con los días de la semana para asociar con cada elementos de la matriz
dia_semana = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
amplitud = 0
amplitud_maxima = 0
temp_min = 0
temp_max = 0
posicion_dia = 0
print()
# Recorro 2 variables, para separar los elementos de cada indice
for temp_minima,temp_maxima in temperatura:
    # voy aumentando esta variable para usarla posteriormente en la lista dia_semana
    posicion_dia += 1
    # Guardo cada elemento en una nueva variable donde se van sumando por separado para calcular promedio
    temp_min += temp_minima
    temp_max += temp_maxima
    # Resto los elementos para sacar la amplitud térmica
    amplitud = temp_maxima - temp_minima
    # Aca guardo el numero mayor registrado en la variable AMPLITUD_MAXIMA
    if amplitud > amplitud_maxima:
        amplitud_maxima = amplitud
        # También guardo la posición del día, para que muestre un día asociado
        dia_mayor_amplitud = posicion_dia
    # Muestro la matriz con todos sus elementos
    print(f"Día: {dia_semana[posicion_dia-1]}\nTemperatura mínima: {temp_minima}°c - Temperatura máxima: {temp_maxima}°c\n")
# Promedios
print(f"\nPromedio temperatura mínima: {temp_min//7}°c")
print(f"Promedio temperatura máxima: {temp_max//7}°c")
# Amplitud máxima con su día asociado
print(f"Día con mayor amplitud térmica: {dia_semana[dia_mayor_amplitud-1]} con {amplitud_maxima}°c")
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

# Ejercicio 8: Notas en Materias de estudiantes
print("\nEjercicio 8: ")
print("Notas por materia:\n")
# Declaro Matriz 5x3
nota_materias = [[7,8.50,10],
                 [6,7,9.33],
                 [7,4,7],
                 [3.50,2,1],
                 [10,7.50,1]]
materia_1 = 0
materia_2 = 0
materia_3 = 0
# Uso la variable posición para recorrer los elementos de cada indice
posicion = 0

for nota_1, nota_2, nota_3 in nota_materias:
    # Separo los elementos en variables individuales y muestro las Notas
    print(f"\nMateria: Programación, nota: {nota_1}\n"\
            f"Materia: Matemática, nota: {nota_2}\n"\
            f"Materia: AySO, nota: {nota_3}")
    # Aca sumo y reasigno los elementos del indice indicado, para calcular promedio
    materia_1 += nota_materias[posicion][0]
    materia_2 += nota_materias[posicion][1]
    materia_3 += nota_materias[posicion][2]
    # Calculo promedio de cada alumno, sumando sus notas y dividiendo por cantidad de alumno
    promedio = (nota_1 + nota_2 + nota_3) / 3
    # La posición cumple la función de reemplazar el nombre del alumno
    # Siendo alumno 1, 2, 3, 4 y 5 respectivamente
    posicion += 1
    print(f"promedio del alumno {posicion}: {promedio:.2f}")
# Promedio final por materia, sumando los indices de cada elemento.
print(f"\nPromedio de la materia Programación: {materia_1}")
print(f"Promedio de la materia Matemática: {materia_2}")
print(f"Promedio de la materia AySO: {materia_3}")
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

print("\nEjercicio 9: ")
print("Ta-Te-Ti\n")
# Ejercicio 9: Ta-Te-Ti

# Declaro la matriz 
tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

# Esta variable definirá si el programa imprime "X" o "O"
turno_x = True
# El contador solo permitirá 9 "turnos"
count = 9
# Se muestra el tablero por pantalla
for fila_en_tablero in tablero:
    print(fila_en_tablero)

# Mientras count sera mayor a 0 , este bucle se iterara
while count > 0: 
    print(f"\nTurnos restantes: {count}")

    # Se pide índice de fila al usuario
    fila = input("Fila (1-3): ")
    # Se valida que el input sea un dígito
    while not fila.isdigit():
        # De no serlo, se vuelve a pedir la entrada
        print("Movimiento no válido: Solo se aceptan números")
        fila = input("Fila (1-3): ")

    # Se pide índice de columna al usuario
    columna = input("Columna (1-3): ")
    # Se valida que el input sea un dígito
    while not columna.isdigit():
        # De no serlo, se vuelve a pedir la entrada
        print("Movimiento no válido: Solo se aceptan números")
        columna = input("Columna (1-3): ")

    # Conversión de tipo de dato de entrada
    fila = int(fila)
    columna = int(columna)

    # Se valida que la entrada no sea un número fuera de los rangos permitidos
    if 1 <= fila <= 3 and 1 <= columna <= 3:
        # se le resta una posición a ambas variables, para que coincidan con los indices del tablero
        fila -= 1
        columna -= 1
        # Si el indice seleccionado presenta el carácter especial "-"
        if tablero[fila][columna] == "-":
           if turno_x: # Si Turno es True le reasigna "X"
                tablero[fila][columna] = "X"
           else: # Si el turno es False le reasigna "O"
                tablero[fila][columna] = "O"
           # Luego invierte el valor de turno_x
           # Si turno_x = True , se reasigna a False
           # Si turno_x = False, se reasigna a True
           turno_x = not turno_x
           # y disminuye el contador 
           count -= 1
        # Si detecta que el índice no tiene como valor "-"
        # No cambia de turno ni descuenta el contador
        else:
           print("Movimiento no valido: Casillero ocupado")
    # Lo mismo si se ingresan valores fuera de rango
    else:
        print("Movimiento no valido: Fuera de rango")

    # Se muestra el tablero por pantalla
    for fila_en_tablero in tablero:
        print(fila_en_tablero)

print("\nFin del juego")
print("-" * 30)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

print("\nEjercicio 10: ")
# Ejercicio 10: Productos vendidos por semana
print("Productos vendidos por semana:\n")
# Creo la Matriz con las cantidades de productos vendidos por día
productos = [[3,2,4,5,2,4,7],
             [5,5,5,4,6,5,3],
             [5,4,7,4,6,7,4],
             [5,4,3,4,5,6,5]]
# Con esta lista les asocio un día
dia_semana = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
venta_por_articulo = 0
venta_por_semana = 0
mas_vendido = 0
posicion_fila = 0
count = 0
dia_con_mas_ventas = 0
# lista para guardar los valores por día
ventas_por_dia = [0] * 7

for fila in productos:
    # Me vi obligado a añadir otro FOR porque no sabía como proseguir
    for i in range(len(fila)):
        # Sumo y reasigno el valor del índice
        ventas_por_dia[i] += fila[i]
    print("Ventas por día:", ventas_por_dia)
    # Recorro cada columna dentro de la fila y voy sumando sus valores
    for columna in fila:
        venta_por_articulo += columna
        venta_por_semana += columna
        # Guardo la suma mas grande en una nueva variable
        if venta_por_articulo > mas_vendido:
            cantidad_vendida_por_semana = venta_por_articulo
            mas_vendido = cantidad_vendida_por_semana
            art_vendido = posicion_fila
    posicion_fila += 1
    count += 1
    # Muestro el artículo más vendido
    print(f"Artículo {count}:")
    # Y la cantidad de este en la semana semana
    print(f"Cantidad vendida por semana: {venta_por_articulo}")
    venta_por_articulo = 0

# Obtengo el máximo
max_ventas = max(ventas_por_dia)
# Obtengo el indice del máximo
indice_max = ventas_por_dia.index(max_ventas)
# Muestro los resultados por pantalla
print(f"\nEl día con más ventas fue: {dia_semana[indice_max]}")
print(f"cantidad vendida: {max_ventas}")
print(f"El articulo mas vendido fue el: {art_vendido+1}")
print(f"con una cantidad de: {cantidad_vendida_por_semana}")
print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

print("\nEjercicio 11: ")
# Ejercicio 11: Encontrar estudiante
print("Encontrar estudiante en lista:\n")

# Se declara la lista con sus elementos
estudiantes = ["Yuliana","Eilen","Carla","Matias","Nicolas","Anabela","Agustina","Pipo","Lola","Betun"]
print(estudiantes)

# Se pide al usuario ingresar un nombre
buscar_estudiante = input("Ingrese nombre del estudiante: ").strip()
# Se valida solo el uso de letras
while not buscar_estudiante.isalpha():
    buscar_estudiante = input("Ingrese nombre del estudiante: ").strip()

# Se recorre la lista indice por indice
for estudiante in estudiantes:
    # Si el nombre ingresado se encuentra dentro de la lista
    if buscar_estudiante.capitalize() in estudiantes:
        # Muestra por pantalla que se encontró el elemento y se muestra su indice 
        print(f"{buscar_estudiante.capitalize()} se encuentra en la lista")
        print(f"En la posición: {estudiantes.index(buscar_estudiante.capitalize())}")
        break
    # Si no encuentra el nombre ingresado en la lista, el bucle vuelve a iterar
    else:
        print("El Estudiante no se encuentra en la lista")
        break

print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

print("\nEjercicio 12: ")
print("Crear lista y ordenarlas\n")
# Ejercicio 12: 
# Creo la lista vacía
numeros = []
count = 1
# Mientras el contador sea menor o igual a 8 , el bucle itera
while count <= 8:
    # Se pide entrada al usuario
    ingresar_numeros = input(f"Ingrese número {count}: ").strip()
    # Se verifica que solo ingrese dígitos
    while not ingresar_numeros.isdigit():
        print("Error: Solo se aceptan números")
        ingresar_numeros = input(f"Ingrese número {count}: ").strip()
    # Conversion de tipo de dato de entrada
    ingresar_numeros = int(ingresar_numeros)
    # Se guarda la variable en la lista
    numeros.append(ingresar_numeros)
    # Contador aumenta en 1
    count += 1
print("Lista original:")
# Se muestra la lista original
print(numeros)
# Ordeno la lista de menor a mayor y se imprime
numeros.sort()
print("De menor a mayor:")
print(numeros)
# Luego de mayor a menor y se imprime
numeros.reverse()
print("De mayor a menor:")
print(numeros)

print("-"*65)
continuar = input("Presione una tecla para continuar: ")

#-----------------------------------------------------------------------------------------------------------

print("Ejercicio 13: ")
print("Puntaje de videojuegos\n")
# Ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# Uso los valores mínimos y máximos de python
# Para encontrar los valores más grandes y más pequeños de las variables
menor = float("inf")
mayor = float("-inf")
# Guardo los valores menores y mayores
for puntaje in puntajes:
    # Si puntaje es menor que la variable menor, a esta se le reasigna el valor de puntaje
    if puntaje < menor:
        menor = puntaje
    #Si puntaje es mayor que la variable mayor, a esta se le reasigna el valor de puntaje
    elif puntaje > mayor:
        mayor = puntaje
# Ordeno la lista de menor a mayor
puntajes.sort()
print(f"Tabla de puntaje:\n{puntajes}")
print(f"Puntaje menor: {menor}\n"\
      f"Puntaje mayor: {mayor}")
# Aclaro que en posición , estoy tomando a partir del valor 0, para mostrar el índice real
print(f"El puntaje 990 se encuentra en la posición {puntajes.index(990)} del ranking")

print("-"*65)

#-----------------------------------------------------------------------------------------------------------

print("Gracias por su tiempo!")