"""Tuplas"""

usuarios = [["Baro",7],["Yuli",1],["Cosme Fulanito",5]]
print(usuarios)

#nombres= []     ESTA ES UNA FORMA DE BUSCAR LOS "NOMBRES" 
#for usuario in usuarios:
    #nombres.append(usuario[0])
#print(nombres)

"""Aqui una mejor forma de hacerlo""" # nombres = [expresion for item in items]

nombres = [usuario[0] for usuario in usuarios]  # al pedirle el indice 0, lo que se le esta
print(nombres)                                   # pidiendo es que devuelva los tipos de datos
                                                # de ese apendice, "Baro" y Transforma la lista
# Recorre el FOR normal, iterando en cada elemento, pero usando solo de parametro el primer indice [0]
# como se le asigno en el ciclo, y por cada elemento, guarda ese atributo en la nueva lista [nombres]
# si el atributo que se le da a la instruccion es el [1] devolvera el numero y no el nombre.

nombres = [usuario for usuario in usuarios if usuario[1] > 2] #aca le pido que me devuelva 
print(nombres)                                                #el elmento entero dentro de la lista
                                  #siempre y cuando [1] uno de los elementos cumpla la condicion > 2 
#Tambien se pueden filtrar elementos e incluso conbinar con la funcion de arriba
nombres = [usuario[1] for usuario in usuarios if usuario[1] > 2]
print(nombres) 