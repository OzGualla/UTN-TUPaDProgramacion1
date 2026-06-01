def suma(*numeros):           # la Instruccion * o Xargs define que se va a hacer una iteracion
    resultado = 0             # el primer atributo se le suma a resultado y se le reasigna el valor
    for numero in numeros:    # a esta variable, el segundo numero vuelve a repetir el bucle
        resultado += numero   
    print(f"el resultado es {resultado}") #IMPORTANTE, el print debe estar fuera del ciclo FOR
                                          # para evitar que se imprima en cada iteracion

suma(3,5)       # No importa cuando atributos mandes a los parametros
suma(6,7,4,5)   # gracias al bucle For y el *
suma(24,9,45)   # la funcion se ejecuta sin problemas

