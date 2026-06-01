def hola():                  # def crea la funcion
    print("Hola mundo!")     # hola es el nombre de esta
    print("Ultimate Phyton") # (): siempre lleva parenticis y 2 puntos


hola()                       # nombrando el nombre de la funcion
                             # y agregandole parentecis la llamo  

def hola(nombre):            # se le puede agregar un PARAMETRO
    print("Hola mundo!")     # que solo se ejecuta dentro de la funcion
    print(f"hola {nombre}")  # entonces cuando la llame puedo modificar el valor
                             # de este PARAMETRO

hola("Yuli")                 # al llamar la funcion declaro 
hola("Cosme Fulanito")       # el ATRIBUTO que esta ejecutara dentro de su bloque 


def hola(nombre, apellido):             # tambien se le puede agregar otros parametros
    print("Hola")                # separados por una coma
    print(f"hola {nombre} {apellido}")  # pero estos tambien deben estar declarados
                                        # dentro de la funcion.

hola("Yuli" , "Almeida")        # los atributos asignados van a respetar
hola("Cosme", "Fulanito")       # el orden de ejecucion de los parametros 
hola("oz" , "")                 # dentro de la funcion, PERO SI USAS ESTO CON VARIOS
hola("" , "Guerrero")           # PARAMETROS SI O SI SE DEBEN DECLARAR AMBOS ATRIBUTOS
