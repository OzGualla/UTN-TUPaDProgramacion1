print("--- Bienvenido al TP N°1 Secuenciales ---")

print("1. Ejercicio 1\n"\
      "2. Ejercicio 2\n"\
      "3. Ejercicio 3\n"\
      "4. Ejercicio 4\n"\
      "5. Ejercicio 5\n"\
      "6. Ejercicio 6\n"\
      "7. Ejercicio 7\n"\
      "8. Ejercicio 8\n"\
      "9. Ejercicio 9\n"\
      "10. Ejercicio 10\n"\
      "0. para salir")

ejercicio = ""

while ejercicio != 0:
    ejercicio = input("Ejercicio: ")
    match ejercicio:
        # Ejercicio 1:
        case "1":
            print("Hola mundo!\n")
        # Ejercicio 2:
        case "2":
            nombre = input("Ingrese su nombre: ")
            print(f"Hola {nombre.capitalize()}!\n")
        # Ejercicio 3:
        case "3":
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            edad = int(input("ingrese edad: "))
            Residencia = input("Ingrese lugar de residencia: ")
            print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {Residencia.capitalize()}\n")
        # Ejercicio 4:
        case "4":
            radio = float(input(f"Ingrese el Radio de un circulo en cm: "))
            PI = float(3.14)
            perimetro = (2*PI) * radio
            area = PI*(radio**2)
            print(f"La circunferencia del circulo es {perimetro:.2f} cm")
            print(f"y su area es de {area:.2f} cm\n")
        # Ejercicio 5:
        case "5":
            segundos = float(input("Ingrese cantidad de segundos: "))
            horas = float(segundos/3600)
            print(f"{segundos:.0f} segundos equivalen a {horas:.2f} horas\n")
        # Ejercicio 6:
        case "6":
            numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
            print(f"{numero} x 0 = {numero * 0}")
            print(f"{numero} x 1 = {numero * 1}")
            print(f"{numero} x 2 = {numero * 2}")
            print(f"{numero} x 3 = {numero * 3}")
            print(f"{numero} x 4 = {numero * 4}")
            print(f"{numero} x 5 = {numero * 5}")
            print(f"{numero} x 6 = {numero * 6}")
            print(f"{numero} x 7 = {numero * 7}")
            print(f"{numero} x 8 = {numero * 8}")
            print(f"{numero} x 9 = {numero * 9}")
            print(f"{numero} x 10 = {numero * 10}\n")
        # Ejercicio 7:
        case "7":
            n1 = int(input("Ingrese primero numero entero diferente de 0: "))
            n2 = int(input("Ingrese segundo numero entero diferente de 0: "))
            print(f"{n1} + {n2} = {n1+n2}\n"\
                f"{n1} - {n2} = {n1-n2}\n"\
                f"{n1} * {n2} = {n1*n2}\n"\
                f"{n1} / {n2} = {n1/n2}\n")
        # Ejercicio 8:
        case "8":
            altura = float(input("Ingrese su altura en metros: "))
            peso = float(input("Ingrese su peso en KG: "))
            imc = peso/(altura**2)
            print(f"\nSu Masa corporal es: {imc:.2f}\n")
            print("Composición corporal	- Índice de masa corporal (IMC)\n"\
                "Peso inferior al normal > Menos de 18.5\n"\
                "Normal -----------------> 18.5 - 24.9\n"\
                "Peso superior al normal > 25.0 - 29.9\n"\
                "Obesidad ---------------> Más de 30.0\n")
        # Ejercicio 9:
        case "9":
            celcius = float(input("Ingrese temperatura en Celcius para pasarla a Farenheint: "))
            farenheint = (9/5) * celcius + 32
            print(f"{celcius:.0f} °Celcius equivalen a {farenheint:.0f} °Farenheint\n")
        # Ejercicio 10:
        case "10":
            n1 = int(input("Ingrese primer numero: "))
            n2 = int(input("Ingrese segundo numero: "))
            n3 = int(input("Ingrese tercer numero: "))
            print(f"El promedio es {(n1+n2+n3)/3:.2f}\n")
        case "0":
            print("Gracias por su tiempo, hasta la proxima!")
            break
        case _:
            print("Opcion invalida, porfavor ingrese un numero entre 1 y 10\n")