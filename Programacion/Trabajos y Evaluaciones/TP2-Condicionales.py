print("--- Bienvenido al TP N°2 Condicionales ---")

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

while ejercicio != "0":
    ejercicio = input("Ejercicio: ")
    match ejercicio:
        # Ejercicio 1
        case "1":
            edad = input("Ingrese su edad: ")
            if edad >= "18":
                print("Es mayor de edad\n")
        # Ejercicio 2
        case "2":
            nota = input("Ingrese su nota: ")
            if nota >= "6":
                print("Aprobado\n")
            else:
                print("Desaprobado\n")
        # Ejercicio 3
        case "3":
            par = int(input("Ingrese un numero par: "))
            if par % 2 == 0:
                print("ingreso un numero par\n")
            else:
                print("Por favor, Ingrese un numero par\n")
        # Ejercicio 4
        case "4":
            edad = int(input("Ingrese se edad: "))
            if 0 <= edad < 12:
                print("Niño\n")
            elif 12 <= edad < 18:
                print("Adolecente\n")
            elif 18 <= edad < 30:
                print("Adulto joven\n")
            elif edad >= 30:
                print("Adulto\n")
            else:
                print("Error\n")
        # Ejercicio 5
        case "5":
            password = input("Ingrese su contraseña (entre 8 a 14 caracteres): ")
            if 8 <= len(password) <= 14:
                print("Ah ingresado una contraseña correcta\n")
            else:
                print("Por favor ingrese una contraseña entre 8 y 14 caracteres\n")
        # Ejercicio 6
        case "6":
            energia = int(input("Ingrese cantidad mensual de KWH: "))
            if energia < 150:
                print("Energia menor que 150 kWh: “Consumo bajo”.\n")
            elif 150 <= energia <= 300:
                print("Energia entre 150 y 300 kWh: “Consumo medio”.\n")
            elif energia >= 300:
                print("Energia mayor que 300 kWh: “Consumo alto”.")
                if energia > 500:
                    print("Considere medidas de ahorro energético\n")
        # Ejercicio 7
        case "7":
            texto = input("Ingrese una frase o palabra: ")
            nuevo_text = len(texto) -1
            if texto.lower()[nuevo_text] in ["a","e","i","o","u"]:
                print(f"{texto}!\n")
            else:
                print(f"{texto}\n")
        # Ejercicio 8
        case "8":
            nombre = input("Ingrese su nombre: ")
            print("1 para ver su nombre en mayusculas\n"\
                  "2 para ver su nombre en minusculas\n"\
                  "3 para ver su inicial en mayusculas")
            opcion = input("-> ")
            if opcion == "1":
                print(f"{nombre.upper()}\n")
            elif opcion == "2":
                print(f"{nombre.lower()}\n")
            elif opcion == "3":
                print(f"{nombre.title()}\n")
        # Ejercicio 9
        case "9":
            print("Usando la Escala Richter del 1 al 7 --->")
            richter = int(input("Ingrese la magnitud del terremoto: "))

            if richter < 3:
                print("Muy leve (imperceptible)\n")
            elif 3 <= richter < 4:
                print("Leve (ligeramente perceptible)\n") 
            elif 4 <= richter < 5:
                print("Moderado (sentido por personas, pero generalmente no causa daños)\n")
            elif 5 <= richter < 6:
                print("Fuerte (puede causar daños en estructuras débiles)\n")
            elif 6 <= richter < 7:
                print("Muy Fuerte (puede causar daños significativos)\n")
            elif richter == 7:
                print("Extremo (puede causar graves daños a gran escala)\n")
        # Ejercicio 10
        case "10":
            hemisferio = input("\nEn que hemisferio se encuentra?\n1- Norte\n2- Sur\n-> ")
            mes = input("Ingrese mes: ")
            dia = input("Ingrese numero de dia: ")
            if hemisferio == "1":
                if ("21" <= dia <= "31" and mes == "12") or ("1" <= dia <= "31" and mes == "1") or ("1" <= dia <= "28" and mes == "2") or ("1" <= dia <= "20" and mes == "3"):
                    print(f"El {dia}/{mes} en el hemisferio Norte es invierno\n")
                elif ("21" <= dia <= "31" and mes == "3") or ("1" <= dia <= "30" and mes == "4") or ("1" <= dia <= "31" and mes == "5") or ("1" <= dia <= "20" and mes == "6"):
                    print(f"El {dia}/{mes} en el hemisferio Norte es primavera\n")
                elif ("21" <= dia <= "30" and mes == "6") or ("1" <= dia <= "31" and mes == "7") or ("1" <= dia <= "31" and mes == "8") or ("1" <= dia <= "20" and mes == "9"):
                    print(f"El {dia}/{mes} en el hemisferio Norte es Verano\n")
                elif ("21" <= dia <= "30" and mes == "9") or ("1" <= dia <= "31" and mes == "10") or ("1" <= dia <= "30" and mes == "11") or ("1" <= dia <= "20" and mes == "12"):
                    print(f"El {dia}/{mes} en el hemisferio Norte es Otoño\n")
            elif hemisferio == "2":
                if ("21" <= dia <= "31" and mes == "12") or ("1" <= dia <= "31" and mes == "1") or ("1" <= dia <= "28" and mes == "2") or ("1" <= dia <= "20" and mes == "3"):
                    print(f"El {dia}/{mes} en el hemisferio Sur es Verano\n")
                elif ("21" <= dia <= "31" and mes == "3") or ("1" <= dia <= "30" and mes == "4") or ("1" <= dia <= "31" and mes == "5") or ("1" <= dia <= "20" and mes == "6"):
                    print(f"El {dia}/{mes} en el hemisferio Sur es Otoño\n")
                elif ("21" <= dia <= "30" and mes == "6") or ("1" <= dia <= "31" and mes == "7") or ("1" <= dia <= "31" and mes == "8") or ("1" <= dia <= "20" and mes == "9"):
                    print(f"El {dia}/{mes} en el hemisferio Sur es Invierno\n")
                elif ("21" <= dia <= "30" and mes == "9") or ("1" <= dia <= "31" and mes == "10") or ("1" <= dia <= "30" and mes == "11") or ("1" <= dia <= "20" and mes == "12"):
                    print(f"El {dia}/{mes} en el hemisferio Sur es Primavera\n")
        case "0":
            print("Gracias por su tiempo.")
            break
        case _:
            print("Ingrese opcion valida\n")         

