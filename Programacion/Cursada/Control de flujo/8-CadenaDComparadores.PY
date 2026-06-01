n1= input("Digite un numero: ")
n2= input("Digite otro numero: ")
nombre = input("Digite su nombre: ")

n1= int(n1)
n2= int(n2)
nombre= str(nombre)

suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1//n2
pote = n1**n2
#las 2 formas de mostrar por pantalla:
mensaje = f"""La suma de {n1} + {n2} es: {suma}. 
La resta de {n1} - {n2} es: {resta}.
La multiplicacion de {n1} * {n2} es: {multi}.
La division de {n1} / {n2} es: {div}.
La potencia de {n1} * {n2} es: {pote}."""

print(mensaje)

print("la suma de: ",n1," + ",n2, "es: ",suma,"\n"
      "la resta de: ",n1," - ",n2, "es: ",resta,"\n"
      "la multiplicacion de: ",n1," * ",n2, "es: ",multi,"\n"
      "la division de: ",n1," // ",n2, "es: ",div,"\n"
      "la potencia de: ",n1," ** ",n2, "es: ",pote)


