""" For sirve para iterar una lista de elementos, en este caso un rango de numeros
auq tambien tiene varias funciones como crear un campo de manera virtual, 
o para buscar elementos en una lista"""

buscar = input("Digite un numero del 0 al 4: ")
buscar = int(buscar)

for numero in range(5):           # Iterador que va del 0 al 4
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:                             # El else en un for se ejecuta si no se ha ejecutado el break
    print("No encontrado", buscar)

for char in "Hola":  # Iterador que recorre cada caracter de la cadena
    print(char)

