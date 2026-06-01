mascotas = ["Haise" , "Ymir" , "Cosme" , "Mandarina"]
mascotas[0] = "Rosado"
print(mascotas)
# print(mascotas[2:]) 
# print(mascotas[-1]) # impreme el ultimo elemente de la lista
print(mascotas[1:2:2]) # desde donde queremos empezar y donde queremos frenar

numeros = list(range(21))
print(numeros[::2]) #impreme los numeros pares
print(numeros[1::2]) #imprime los numeros impares

my_list = []
my_list2 = list()

my_list.append(" y su poderosa Mandarina")
my_list.insert( 0 , "La increible Yuli")
my_other_list = my_list.copy()
my_list.remove(" y su poderosa Mandarina")
yuli = my_list.pop(0)

print(my_list)
print(my_other_list)
print(yuli)
