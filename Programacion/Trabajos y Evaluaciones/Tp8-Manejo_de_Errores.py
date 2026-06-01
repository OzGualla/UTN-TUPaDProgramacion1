
""" Tp8 - Manejo de Errores """
# =========================
# Declaración de funciones:
# =========================

def validar_numeros(numero):
    """
    Recibe como parámetro: dígito (str)
    Y retorna: numero (int) validado
    """
    while True:
        # Validar que sea número (permite "-")
        if numero.lstrip("-").isdigit():
            numero = int(numero)

            # Validar que NO sea 0
            if numero == 0:
                print("Error: No se puede dividir por 0")
                numero = input("Ingrese nuevamente: ")
            else:
                return numero
        else:
            print("Solo se aceptan números")
            numero = input("Ingrese nuevamente: ")

# ============
# Ejercicio 1 :
# ============

# Se aisló el código entre """ """ para evitar un error y permitir la ejecución de TP
"""
a = 10
b = input("Introduce un número: ")
result = a / b # Error: TypeError - "a" es un integer y "b" es un string, 
print(f"Resultado: {result}")  # No permite la division por que los tipos de datos son incompatibles


numbers = [1, 2, 3]
print(numbers[5]) # Error: IndexError - Se esta intentando acceder a un indice inexistente en la lista
"""

# ============
# Ejercicio 2:
# ============

print("\n=== Ejercicio 2 ===")

a = 10

# Utilizo una función para validar la entrada correctamente
b = validar_numeros(input("Introduce un número: "))

result = a / b # Se elimina el TypeError haciendo una conversion de tipo de dato 

print(f"Resultado: {result:.2f}") # Y se imprime el resultado correctamente

numbers = [1, 2, 3]

numbers.extend([4, 5, 6, 7])  # Extiendo la lista para alcanzar el indice requerido

print(numbers[5])  # para alcanzar el indice requerido

""" La otra opción es cambiar el indice al cual se quiere acceder
    print(numbers[2]) pero si el requerimiento es acceder al indice 5, me pareció correcta mi solución"""

# ============
# Ejercicio 3:
# ============

print("\n=== Ejercicio 3 ===")

# Utilize el try/except para evitar el error y permitir la continuación del TP
try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b # Error: TypeError - "a" es un integer y "b" es un string, 
    print(f"Resultado: {result}")  # No permite la division por que los tipos de datos son incompatibles


    numbers = [1, 2, 3]
    print(numbers[5]) # Error: IndexError - Se esta intentando acceder a un indice inexistente en la lista

except:
    print("Los 2 ejercicios contienen un error, e impedirán la ejecución del código")

# ============
# Ejercicio 4:
# ============

print("\n=== Ejercicio 4 ===")

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b # Error: TypeError - "a" es un integer y "b" es un string, 
    print(f"Resultado: {result}")  # No permite la division por que los tipos de datos son incompatibles

except TypeError:
    print("El tipo de dato no es compatible")

try:
    numbers = [1, 2, 3]
    print(numbers[5])

except IndexError:
    print("El indice requerido no existe")


# ============
# Ejercicio 5:
# ============

print("\n=== Ejercicio 5 ===")

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b # Error: TypeError - "a" es un integer y "b" es un string, 
    print(f"Resultado: {result}")  # No permite la division por que los tipos de datos son incompatibles


    numbers = [1, 2, 3]
    print(numbers[5]) # Error: IndexError - Se esta intentando acceder a un indice inexistente en la lista

except TypeError:
    print("El tipo de dato no es compatible")

except IndexError:
    print("El indice requerido no existe")

except ZeroDivisionError:
    print("Error: división por cero")

else:
    print("El programa se ejecutó correctamente")

finally:
    print("Ejecución finalizada")

# ============
# Ejercicio 6:
# ============

print("\n=== Ejercicio 6 ===")

try:
    numero = int(input("Ingrese un número: "))
    print("\nNumero ingresado:", numero)

except ValueError:
    print("Debe ingresar un número válido")

except Exception as e:
    print("Se produjo un error inesperado: ", type(e).__name__)

# ============
# Ejercicio 7:
# ============

print("\n=== Ejercicio 7 ===")

while True:
    try:
        numero = int(input("Ingrese un numeró: "))
        print("\nNumero ingresado: ", numero)
        break
    
    except ValueError:
        print("Debe ingresar un número válido")
            
    except Exception as e:
        print(f"Se produjo un error inesperado - Error: ", type(e).__name__)


