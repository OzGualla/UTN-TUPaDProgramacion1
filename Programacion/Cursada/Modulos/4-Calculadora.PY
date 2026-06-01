n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")

n1 = int(n1) # convierte a entero
n2 = int(n2) # convierte a entero

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 // n2

mensaje = f"""para los numeros {n1} y {n2} Los resultados son:
la suma es {suma}.
la resta es {resta}.
la multiplicacion es {multi}.
la division es {div}."""             #IMPORTANTE la f permite usar variables dentro del string

print(mensaje)

