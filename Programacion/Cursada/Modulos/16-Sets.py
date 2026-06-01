error_set = {} # Esto crea un diccionario ojo!
print(type(error_set))
my_set = {1,1,2,3,3,4,5,5,6,7,8,9,9}
my_other_set = set()

lista_a_set = ["a","a","b","c","c","d"]
set_de_lista = set(lista_a_set) # Crea un set de una lista, eliminando los repetidos
print(set_de_lista) 

# los elementos no están ordenados, no hay indice
my_other_set.add("Oz")   
my_other_set.add("Yuli") # Agregar elemento
my_other_set.add("Yuli") # No agrega repetidos
my_other_set.add("Cosme")
my_other_set.add("Ymir")
print(my_other_set)

my_other_set.remove("Yuli") # Elimina elemento, error si no existe
print(my_other_set)

my_other_set.discard("Nono") # Elimina elemento, no da error si no existe
print(my_other_set)

print(len(my_other_set))
my_other_set.clear() # Deja el set vació
print(my_other_set)

my_other_set.add(1)
my_other_set.add(3)
my_other_set.add(9)

for i in my_set:
    print(i)

if "Yuli" in my_other_set:
    print("Si")
else:
    print("No")

union_sets = my_set | my_other_set # Método Union elimina duplicados
print(union_sets)

union_sets = my_set & my_other_set # Método Intersección muestra los elementos en común
print(union_sets)

union_sets = my_set - my_other_set # Método Diferencia quita los elementos del 2 conjunto, 
print(union_sets)                  #que existan en el primero

union_sets = my_set ^ my_other_set # Método Diferencia Simétrica quita los elementos que se encuentran
print(union_sets)                  # En ambos conjuntos

# Subconjunto
print(my_other_set.issubset(my_set)) # Si todos los elementos my_other_set pertenecen a my_set set True o False

# Superconjunto
print(my_other_set.issuperset(my_set)) # Si my_set forma parte de my_other_set