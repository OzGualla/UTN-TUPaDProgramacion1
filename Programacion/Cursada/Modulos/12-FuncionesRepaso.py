#Las Funciones sirven para resolver un bloque o problema concreto, y tienen la ventaja
#de evitar errores ya que al llamarla, no hace falta volver a reescribirlas.

def show_tetx():         #crear una funcion basica
    print("Hola mundo")

show_tetx()             #llamar a la funcion

def suma(num1,num2):   #se le pueden asignar parametros
    print(num1+num2)  #para que ejecuten codigo

suma(14,16)         #y se le pasa valores en forma de argumentos

def nombres(nombre, apellido, alias = "Sin Alias"): #se le puede asignar un valor default a un parametro
    print(f"{nombre} {apellido} {alias}")           #si no se le da un argumento, mostrara su valor
                                                    #por defecto
nombres("Baro", "Vero")

def textos(*text):          # el * permite agregar infinidad de parametros
    for texto in text:      # asi que los puedo iterar con un for
        print(texto)

textos("Hola","Baro","Vero","Trolo")  # asi pasa por cada argumento (No es una lista)
                                      # es una funcion con PARAMETROS ARBITRARIOS

def suma_return(n1,n2,n3):
    nueva_suma = n1+n2+n3
    return nueva_suma                 # RETURN devuelve el valor

resultado = suma_return(15,20,35)    # para conseguir eso, se lo asignamos a una nueva variable
print(resultado)                     #si no usamos el return, no imprime nada




