edad = input("Ingrese su edad: ")
edad = int(edad)

if edad > 120:
    print("Probablemente estas fallecido")
elif edad >= 65 and edad <=120:
    print("Eres jubilado")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

