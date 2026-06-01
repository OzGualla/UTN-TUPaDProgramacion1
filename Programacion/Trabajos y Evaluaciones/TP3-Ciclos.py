print("--- Bienvenido al trabajo practico de repetitivas ---")
print("1:  Mostrar numeros de 0 al 100 inclusive\n" \
      "2:  Muestra la cantidad de digitos del numero ingresado\n" \
      "3:  Muestra la suma de todos los numeros intermedios entre 2 enteros\n" \
      "4:  Suma todos los numeros ingresados (0 para mostrar el resultado)\n" \
      "5:  Adivina el numero secreto!\n" \
      "6:  Cuenta regresiva de 100 a 0\n" \
      "7:  Muestra la suma de todos los numeros intermedios entre 0 y el numero elegido\n" \
      "8:  Muestra todos los numeros -> Pares, impares, positivos y negativos de 100 numeros ingresados\n" \
      "9:  Muestra la media de 100 numeros ingresados\n" \
      "10: Invierte el orden del la cadena ingresada\n" \
      "11: Invierte el ordel del numero ingresado\n" \
      "0:  0 para salir!")

while True:
    ejercicio = input("Elija el ejercicio: ")
    if ejercicio != "0":
        match ejercicio:
            case "1":
                #1
                num = 0
                while num <= 100:
                    print(num)
                    num += 1
            case "2":
                #2
                num = input("\nIngrese un numero entero: ")
                print(f"La cantidad de digitos que contiene el numero {num} es {len(num)}")
            case "3":
                #3
                n1 = int(input("\nIngrese primer numero: "))
                n2 = int(input(f"Ingrese segundo numero mayor a {n1}: "))
                sumatoria = 0
                while n2 < n1:
                    print("El segundo numero debe ser mayor al primero: ")
                    n2 = int(input(f"Ingrese un numero mayor a {n1}: "))

                for i in range(n1+1 , n2):
                    sumatoria += i
                print(f"La Suma de los numeros intermedios entre {n1} y {n2} es {sumatoria}")
            case "4":
                #4
                CORTE = 0
                n1 = int(input(f"\nIngrese un numero ({CORTE} para salir): "))
                suma = 0
                while n1 != CORTE:
                    n1 = int(input("Ingrese otro numero: "))
                    suma += n1
                print(f"La suma total de los numeros ingresados es = {suma}")
            case "5":
                #5
                import random
                n1 = ""
                intentos = 0
                num_random = random.randint(0, 9)
                while n1 != num_random:
                    n1 = int(input("\nAdivina el numero secreto!: "))
                    intentos += 1
                    if n1 == num_random:
                        print(f"Felicidades! Adivinaste el numero secreto! era {num_random}")
                        break
                    elif n1 < (num_random):
                        print("El numero que ingresaste es bajo!")
                    elif n1 > (num_random):
                        print("El numero que ingresaste es alto!")
                print(f"Te llevo tan solo {intentos} itento/s!")
            case "6":
                #6
                num = 98
                while num > 0:
                    print(num)
                    num -= 2
            case "7":
                #7
                num = int(input("Ingrese un numero: "))
                sumatoria = 0
                for i in range(num):
                    sumatoria += i 
                print(f"La suma de todos los numeros comprendidos entre 0 y {num} es = {sumatoria}")
            case "8":
                #8
                cont = 0
                positivos = 0
                negativos = 0
                pares = 0
                impares = 0
                num = 0
                while cont < 10:
                    cont += 1
                    num = int(input(f"Ingrese el numero {cont}: "))
                    if num > 0:
                        positivos += 1
                        if num % 2 == 0:
                            pares += 1
                        elif num % 2 != 0:
                            impares +=1
                    if num < 0:
                        negativos += 1
                        if num % 2 == 0:
                            pares += 1
                        elif num % 2 != 0:
                            impares +=1
                print(f"Los numeros positivos ingresados fueron {positivos}")
                print(f"Los numeros negativos ingresados fueron {negativos}")
                print(f"Los numeros pares ingresados fueron {pares}")
                print(f"Los numeros impares ingresados fueron {impares}")
            case "9":
                #9
                cont = 0
                num = 0
                sumatoria = 0
                while cont < 10:
                    cont += 1
                    num = int(input(f"Ingrese el numero {cont}: "))
                    sumatoria += num
                print(f"El promedio de los numeros ingresados es: {sumatoria/100}")
            case "10":
                #10
                num = str(input("Ingrese la cadena de texto a invertir: "))# Lo que realmente esta ingresando el usuario
                num_reverse = ""                                 # es una cadena de texto
                for digito in num:                              # para poder recorrerla con un ciclo For
                    if digito != (""):                         # me aseguro que la condicion siempre se cumpla
                        num_reverse = digito + num_reverse    # y a la nueva variable, le sumo el valor del caracter
                print(num_reverse)                           # de la entrada delante del nuevo de la nueva variable.
                                                            # ejemplo: num = hola
                                                        # num_reverse = h = o+h 
                                                        # oh = oh + l 
                                                        # loh = a+loh
                                                        # num_reverse = aloh
            case "11":
                #10 segunda opcion

                numero = int(input("Ingrese un numero entero: "))
                numero_absoluto = abs(numero)

                numero_invertido = 0
                # El numero ingresado 512
                while numero_absoluto > 0:        # Todo numero dividido / 10 te va a dar el ultimo numero como decimal o entero
                    digito = numero_absoluto % 10 # Asi obetenes el ultimo valor ingresado 115 / 10 = 11.5 (es resto es 5)
                    numero_invertido = numero_invertido * 10 + digito #Aca se guarda el resto de la div. en este caso 5 despues 1 y 2
                    numero_absoluto //= 10       # Al hacer divicion entera // 10 le quita el decimal 11.5 pasa a ser 11
                if numero < 0:
                    numero_invertido = -numero_invertido # Y si el numero es negativo, el abosuluto lo convierte en positivo
                print(numero_invertido)                  # asi que se le vuelve a asignar la negacion   
            case _:
                print("Opcion no valida! Intenta denuevo!\n")
    else:
        print("Gracias por participar!")
        break            