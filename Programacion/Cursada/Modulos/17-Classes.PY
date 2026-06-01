""" Classes """ 

class MyEmptyPerson:     # Definir una classe, el nombre con Mayus

    pass # es una declaración nula que funciona como un marcador de posición, 
         #indicando al intérprete que no haga nada y evita errores
class MyPerson:
    def __init__(self, name, surname): # __ init__ es el constructor de los objetos dentro de una classe
        self.name = name             # self es el primer parametro obligatorio que una classe debe llevar
        self.surname = surname      # para trabajar con sus parametros
# Reasignar el valor del parametro a self. para que la clase sepa que es un valor propio de ella  

my_person = MyPerson("Baro", "Vero")
print(f"{my_person.name} {my_person.surname}")
