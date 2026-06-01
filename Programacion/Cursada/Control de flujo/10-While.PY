numero = 1

while numero < 100:     # Itera hasta que se deja de cumpli la condicion
    print(numero)
    numero *= 2         # Equivalente a numero = numero * 2


comando = ""            # Mientras el comando sea diferente de "salir" seguira pidiendo comandos

while comando.lower() != "salir":
    comando = input("$ ")
    print("El comando es: ", comando.lower())

print("Fin")