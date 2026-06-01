def hola():                  # def crea la funcion
    print("Hola mundo!")     # hola es el nombre de esta
    print("Ultimate Phyton") # (): siempre lleva parenticis y 2 puntos


hola()                       # nombrando el nombre de la funcion
                             # y agregandole parentecis la llamo  

def hola(nombre):            # se le puede agregar un PARAMETRO
    print("Hola mundo!")     # que solo se ejecuta dentro de la funcion
    print(f"hola {nombre}")  # entonces cuando la llame puedo modificar el valor
                             # de este PARAMETRO

hola("Yuli")

def suma(num1,num2):   #se le pueden asignar parametros
    print(num1+num2)  #para que ejecuten codigo

def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != (" "):
            nuevo_texto += char
    return nuevo_texto