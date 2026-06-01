my_dict = {}
my_other_dict = dict()

my_dict = {"Baro"     :    "Oz"    , "Marrona" : "Ymir" , "La poderosa" : "Yuli"}
           #Key o llave   #Valor
my_other_dict = {
"Ay amor" : "Cosme" ,
"Rosado" : "Haise" ,
"Roba Maridos" : {"leandro" , "mati" } #SETS dentro de un diccionario
}

print(len(my_other_dict)) #Cantidad de llaves asignadas , en este caso 3
print(my_dict["La poderosa"]) # Al llamar a la llave, muestra su valor
my_dict["Baro"] = "Mariano" # Reasignar el valor de una key
print(my_dict)
my_dict["Calle"] = "Beltran" # Agregar llave-Valor al dict

# Este método agrega varias llave-valor al dict
my_other_dict.update({"Chizito" : "Thor" , "Orejon" : "Loki" , "Mortadelita" : "Estrella"})
print(my_other_dict)

# Agregar clave - valor por input
for i in range(2):
    apodo = input("Ingrese apodo: ")
    nombre = input("Ingrese Nombre: ")
    my_other_dict[apodo] = nombre # Agrega llave-Valor al dict
print(my_other_dict)

del my_dict["Marrona"] # Al asignarle una llave a la palabra reservada DEL
                       # Solo borra esa llave-Valor y no todo el dict
print(my_other_dict.items()) #Listado de Keys y Values correspondientes
clave_valor = my_other_dict.items() # devuelve un iterable
lista_claves_valor = list(clave_valor) 
for par in lista_claves_valor:
    print("\n",par)

print(my_other_dict.keys()) # Muestra solo las Keys
claves = my_other_dict.keys() # devuelve un iterable
lista_claves = list(claves) 
print("\n",lista_claves)

print("\n",my_other_dict.values()) # Muestra solo los valores
claves = my_other_dict.values()
lista_claves = list(claves)
print("\n",lista_claves)

new_dict = dict.fromkeys(("Baro" , "La poderosa")) #Crear nuevo dict con keys sin valor
other_new_dict = my_other_dict.fromkeys(("ay amor" , "Rosado"))

print(new_dict)
print(other_new_dict)

""".get() es un método de los diccionarios que sirve para obtener un valor usando una clave, 
pero sin romper el programa si la clave no existe.

recuento["hola"] = recuento.get("hola", 0) + 1

- “Busca la clave "hola" en el diccionario”
- Si existe → devuelve su valor
- Si NO existe → devuelve 0 (el valor por defecto que vos elegís)
- recuento.get("hola", 0) → como no existe → devuelve 0
- 0 + 1 = 1
- ahora "hola" sí existe → devuelve 1
- 1 + 1 = 2"""