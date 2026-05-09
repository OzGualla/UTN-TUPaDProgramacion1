
""" Tp6- Funciones """
# -----------------------
# definición de funciones
# -----------------------
"""Aclaración: 
En los ejercicios que piden impresión por pantalla, sera la función la que se encargue
de hacer el print.
En los ejercicios que pidan devolución de valor, la función lo retornara, y los print se ejecutaran
fuera de la función"""

# --- Punto 1 ---
def imprimir_hola_mundo():
    """
    Imprime un mensaje por pantalla
    """
    print("Hola Mundo!")

# --- Punto 2 ---
def saludar_usuario(nombre):
    """
    Imprime un mensaje por pantalla
    Recibe como parámetro:
    nombre (str)
    Y retorna:
    un string mostrando el valor del parámetro 
    """
    return f"Hola {nombre}!"

# --- Punto 3 ---
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Imprime un mensaje por pantalla
    Recibe como parámetros
    nombre (str), apellido (str), edad (int), residencia (str)
    Y retorna:
    Un string mostrando los valores de los parámetros
    """
    print(f"\nSoy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}")

# --- Punto 4 ---
def calcular_area_circulo(radio):
    """
    Calcula el área de un circulo
    Recibe como parámetros:
    Radio (int o float)
    Y retorna:
    el área del circulo (float)
    """
    PI = float(3.14)
    area = PI*(radio**2)
    return area 

# Ambas funciones reciben como parámetro el radio declara en la entrada
def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un circulo
    Recibe como parámetros:
    radio (int o float)
    Y retorna:
    el perímetro del circulo (float)
    """
    PI = float(3.14)
    perimetro = (2*PI) * radio
    return perimetro

# --- Punto 5 ---

def segundos_a_horas(segundos):
    """
    Calcula el equivalente de segundos, en horas
    Recibe como parámetro:
    segundos (int)
    Y retorna:
    el equivalente en horas (float)
    """
    horas = segundos/3600
    # Al retornar el valor horas, lo guardo en una variable
    return horas

# --- Punto 6 ---

def tabla_multiplicar(numero):
    """
    Calcula la multiplicación del parámetro
    por una secuencia de números (1 a 10)
    Recibe como parámetro:
    numero (int)
    Y retorna:
    un string mostrando el valor del parámetro multiplicado
    """
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

# --- Punto 7 ---

def operaciones_basicas(a,b):
    """
    Calcula suma, resta, producto y división de dos números
    Recibe como parámetro:
    a, b (int)
    Y retorna:
    Una tupla con los valores de las operaciones
    """
    suma = a+b
    resta = a-b
    producto = a*b
    division = a/b
    return (suma,resta,producto,division)

# --- Punto 8 ---

def calcular_imc(peso,altura):
    """
    Calcula el indice de masa corporal
    Recibe como parámetro:
    peso, altura (int o float)
    Y Retorna
    El valor del imc
    """
    imc = peso/(altura**2)
    return imc

# --- Punto 9 ---

def celsius_a_fahrenheit(celsius):
    """
    Calcula el equivalente de grados Celsius,
    en grados Fahrenheit
    Recibe como parámetro:
    celsius (int)
    Y retorna:
    el equivalente en Fahrenheit (float)
    """
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# --- Punto 10 ---

def calcular_promedio(a, b, c):
    """
    Calcula el promedio sumando los parámetros 
    y dividiendo por la cantidad de parámetros recibidos
    Recibe como parámetro:
    a,b,c int (int o float)
    Y retorna:
    el valor del promedio
    """
    promedio = (a + b + c) / 3
    return promedio

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
        print("\nSolo se aceptan números")
        numero = input("Ingrese nuevamente: ")
    numero = int(numero)
    return numero

# Para validar números negativos
def validar_numeros_negativos(numero):
    """
    Si el parámetro comienza con "-"
    lo ignora y verifica si la entrada no es un dígito
    si no lo es no acepta la entrada y vuelve a pedir el input
    Recibe como parámetro:
    numero (str)
    Y retorna:
    numero (int) validado
    """
    while not numero.lstrip("-").isdigit():
        print("\nSolo se aceptan números")
        numero = input("Ingrese nuevamente: ")
    numero = int(numero)
    return numero

def validar_no_acepta_n_negativos():
    """
    Si el parámetro comienza con "-"
    lo ignora y verifica si la entrada no es un dígito
    si no lo es no acepta la entrada y vuelve a pedir el input.

    VALIDA NÚMEROS NEGATIVOS PERO NO LOS ACEPTA COMO ENTRADA
    
    Recibe como parámetro:
    numero (str)
    Y retorna:
    numero (int) validado
    """
    while True:
        # Validar que sea número (permite "-")
        if numero.lstrip("-").isdigit():
            numero = int(numero)

            # Validar que NO sea negativo
            if numero < 0:
                print("Error: No se puede agregar una cantidad menor a 0")
                numero = input("Ingrese nuevamente: ")
            else:
                return numero
        else:
            print("Solo se aceptan números")
            numero = input("Ingrese nuevamente: ")

# Para validar números decimales
def validar_numero_flotante(numero):
    """
    Si el parámetro tiene un "."
    lo ignora y verifica si la entrada no es un dígito
    si no lo es no acepta la entrada y vuelve a pedir el input
    Recibe como parámetro:
    numero (str)
    Y retorna:
    numero (float) validado
    """
    # Evita que se ingrese mas de 1 "." ejemplo = 1.7.0 no lo valida
    while not numero.count(".") <= 1 and numero.replace(".","").isdigit():
        print("\nSolo se aceptan números")
        numero = input("Ingrese nuevamente: ")
    numero = float(numero)
    return numero

# Este input es solo para poder visualizar el resultado del ejercicio, 
# Sin que la visualización del siguiente moleste al usuario
def ejercicio_siguiente():
    input("Presione una tecla para continuar. ")

# -------------------
# Programa Principal
# -------------------

# --- Punto 1 ---
print("\nEjerció 1:")
imprimir_hola_mundo()

# --- Punto 2 ---
print("\nEjerció 2:")
print(saludar_usuario("Marcos"))

# --- Punto 3 ---
print("\nEjerció 3:")
# A partir de este punto, se validan todas las entradas,
# Para evitar posibles errores.
nombre = validar_letras(input("Nombre: "))

apellido = validar_letras(input("Apellido: "))

edad = validar_numeros(input("Edad: "))

residencia = validar_letras(input("Residencia: "))

informacion_personal(nombre,apellido,edad,residencia)

ejercicio_siguiente()

# --- Punto 4 ---
print("\nEjerció 4:")
radio = validar_numero_flotante(input(f"Ingrese el Radio de un circulo en cm: "))
area_calculada = calcular_area_circulo(radio)
perimetro_calculado = calcular_perimetro_circulo(radio)
print(f"\nEl area es de {area_calculada:.2f} cm")
print(f"La circunferencia es de {perimetro_calculado:.2f} cm")

ejercicio_siguiente()

# --- Punto 5 ---
print("\nEjerció 5:")
segundos = validar_numeros(input(f"Ingrese segundos para convertir a horas: "))
conversion_a_horas = segundos_a_horas(segundos)
print(f"\n{segundos} segundos equivalen a {conversion_a_horas:.2f} horas")

ejercicio_siguiente()

# --- Punto 6 ---
print("\nEjerció 6:")
numero_a_multiplicar = validar_numeros(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_a_multiplicar)

ejercicio_siguiente()

# --- Punto 7 ---
print("\nEjerció 7:")
# En este punto el primer numero puede tomar cualquier valor que el usuario desee, incluido números negativos
primer_numero_validado = validar_numeros_negativos(input("Ingrese primer numero: "))

while True:
    # En este punto se usa una validación extra para que el usuario no ingrese un 0
    # y la division resulte en un error. 
    segundo_numero_operacion = input("Ingrese un segundo numero diferente a 0: ")
    segundo_numero_validado = validar_numeros_negativos(segundo_numero_operacion)
    if segundo_numero_validado == 0:
        print("El numero debe ser diferente a 0")
        continue

    break

# Se devuelve una tupla y se guarda en una variable
resultado = operaciones_basicas(primer_numero_validado, segundo_numero_validado)

# Se muestran los resultados de forma clara
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Producto: {resultado[2]}")
print(f"División: {resultado[3]:.2f}")

ejercicio_siguiente()

# --- Punto 8 ---
print("\nEjerció 8:")
peso = validar_numero_flotante(input("Ingrese su peso en KG: "))
altura = validar_numero_flotante(input("Ingrese su altura en metros: "))
# Esta validación es para forzar al usuario a ingresar un número decimal "n.n"
# De no hacerlo, el resultado del IPC resultara en 0
# El valor máximo de 3 mts, es de referencia, wn teoría imposible que un humano lo pase.
while altura > 3:
    print("Error: Su altura debe ingresarse en MTS (Ejemplo: 2 o 1.70)")
    print("Valor máximo permitido: 3 Mts")
    altura = validar_numero_flotante(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso,altura)
# Se agrego una tabla, para que el usuario pueda ubicar su imc cómodamente
print(f"\nSu Masa corporal es: {imc:.2f}\n")
print("Composición corporal	- Índice de masa corporal (IMC)\n"\
    "Peso inferior al normal > Menos de 18.5\n"\
    "Normal -----------------> 18.5 - 24.9\n"\
    "Peso superior al normal > 25.0 - 29.9\n"\
    "Obesidad ---------------> Más de 30.0\n")

ejercicio_siguiente()

# --- Punto 9 ---

print("\nEjerció 9:")
grados_celsius = validar_numeros_negativos(input("Ingrese temperatura en Celsius para pasarla a Fahrenheit: "))
# Se guarda el valor retornado en la variable
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
# Y se muestra prolijamente por pantalla
print(f"{grados_celsius:.0f} °Celsius equivalen a {grados_fahrenheit:.0f} °Fahrenheit\n")

ejercicio_siguiente()

# --- Punto 10 ---

print("\nEjerció 10:")
# Se utiliza una lista para guardar los números ingresados
promedio = []

for i in range(3):
    numero = validar_numeros_negativos(input(f"Ingrese el número {i+1}: "))
    promedio.append(numero)

# como argumento, se le pasan los valores por indice a la función
promedio_calculado = calcular_promedio(promedio[0], promedio[1], promedio[2])
print(f"{promedio_calculado:.2f}")

