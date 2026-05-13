
""" Tp9 - Manejo de Archivos """

# ========================
# Declaración de variables
# ========================

def validar_letras(palabra):
    """
    Recibe como parámetro: palabra (str)
    Y retorna: palabra (str) validado
    """
    while not palabra.isalpha():
        print("\nSolo se aceptan letras")
        palabra = input("Ingrese nuevamente: ")
    return palabra
        
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
            if numero <= 0:
                print("Error: La cantidad no puede ser menor o igual a 0")
                numero = input("Ingrese nuevamente: ")
            else:
                return numero
        else:
            print("Solo se aceptan números")
            numero = input("Ingrese nuevamente: ")

def validar_numero_flotante(numero):
    """
    Recibe como parámetro: numero (str)
    Y retorna: numero (float) validado
    """
    while True:
        numero = numero.strip()
        try:
            valor = float(numero)
            if valor <= 0:
                print("Error: Solo se pueden ingresar números positivos")
            else:
                return valor
        except ValueError:
            print("Error: Solo se pueden ingresar números positivos")

        numero = input("Ingrese nuevamente: ")

# ==================
# Programa Principal
# ==================

# Actividad 1:
try:
    # Utilizo with open, para asegurarme que el archivo siempre va a cerrarse
    with open("productos.txt", "w", encoding = "utf-8") as archivo:

        # Ingreso producto, precio, cantidad al archivo 
        archivo.write("Harina,120.5,10\n")
        archivo.write("Fideos,105.3,5\n")
        archivo.write("Arroz,75,20\n")

# Esta excepción es por si falla el directorio o la sincronización del archivo.txt
except FileNotFoundError:
    print("Error: Archivo no encontrado")

# En caso de ocurrir otro tipo de error
except Exception as e:
    print("Ha ocurrido el siguiente error: ", type(e).__name__)

# Si se crea el archivo correctamente, se informa al usuario
else:
    print("\nArchivo: 'productos.txt' creado\n")
 
# Se utilizara una lista para guardar los nombres de los productos agregados en la actividad 3
productos_existentes = []

# Actividad 2:
print("=== Lista de productos ===\n")
 
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # limpio los saltos de línea y separa la lista
        productos = linea.strip().split(",")

        nombre = productos[0].lower()
        # Aca se guardan los productos en la lista declarada
        productos_existentes.append(nombre)

        """Aca la idea principal era hacerlo de la siguiente manera:
        productos_unidos = " | ".join(productos)
        Pero me encontré con el problema de que .join une los valores de la lista
        y no podia mostrarlos con el formato requerido"""

        # Opte por la siguiente forma, para cumplir con la actividad 2
        nombre = productos[0]
        precio = productos[1]
        cantidad = productos[2]

        print(f"Producto: {nombre} | Precio: ${float(precio):.2f} | Cantidad: {cantidad}")

# Actividad 4:

# lista para diccionarios
productos = []

with open("productos.txt", "r", encoding = "utf-8") as archivo:
    # Se crea un diccionario para almacenar los productos en forma de clave:valor
    for linea in archivo:

        dato = linea.strip().split(",")

        diccionario = {
            "nombre": dato[0],
            "precio": dato[1],
            "cantidad": dato[2]
        }
        # y se agregan a la lista
        productos.append(diccionario)

# Actividad 3:

# El usuario puede agregar la cantidad de artículos que desee
cantidad_de_productos = validar_numeros(input("\nCuantos productos desea agregar? -> "))

with open("productos.txt", "a", encoding = "utf-8") as archivo:

    for producto in range(cantidad_de_productos):

        print(f"Producto n°{producto+1}/{cantidad_de_productos}")

        # El usuario puede agregar nuevos artículos
        while True:
            agregar_producto = validar_letras(input("Ingrese Producto: "))

            # Se verifica si el producto a agregar ya existe dentro de la lista
            if agregar_producto.lower() in productos_existentes:
                print("Error: El producto ya existe")
            else:
                productos_existentes.append(agregar_producto.lower())
                break

        agregar_precio = validar_numero_flotante(input("Ingrese Precio: "))

        agregar_cantidad = validar_numeros(input("Ingrese Cantidad: "))

        # Se agregan al archivo separados por ","
        archivo.write(f"{agregar_producto},{agregar_precio},{agregar_cantidad}\n")
        # Guardar también en la lista de diccionarios
        productos.append({
            "nombre": agregar_producto,
            "precio": agregar_precio,
            "cantidad": agregar_cantidad
        })


# Actividad 5:

# se le permite al usuario buscar un producto 
buscar_producto = validar_letras(input("\nIngrese el nombre del producto a buscar: "))

# Esta variable se actualiza dentro del siguiente For
producto_encontrado = False

try:
    # Si el producto existe dentro del diccionario, muestra sus clave:valor
    for producto in productos:
        if producto["nombre"].lower() == buscar_producto.lower():
            producto_encontrado = True
            print(f"\nProducto: {producto['nombre'].capitalize()} | Precio: ${float(producto['precio']):.2f} | Cantidad: {producto['cantidad']}")
            break
    # Si no existe dentro del diccionario, muestra un mensaje de error
    if not producto_encontrado:
        print(f"\nError: El producto '{buscar_producto}' no existe")

except Exception as e:
    print(f"\nHa ocurrido un error inesperado: ", type(e).__name__)

# Actividad 6:
# Por ultimo se actualiza el archivo.txt con los cambios realizados

with open("productos.txt", "w", encoding="utf-8") as archivo:

    for producto in productos:

        archivo.write(
            f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        )

print("\nArchivo 'productos.txt' actualizado correctamente")