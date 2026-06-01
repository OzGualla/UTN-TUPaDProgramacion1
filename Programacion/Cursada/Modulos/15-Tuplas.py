
def func(): # Una función que devuelve varios elementos
    return 1,2,3

a, b, c = func()
print(a, b, c)

# Crear tupla
my_tuple = tuple()
my_other_tuple = ()
# Empaquetar y crear tupla
tupla_empaquetada = 10,20,30
# Convertir lista a tupla
mi_lista = ["Mariano","Yuliana"]
lista_a_tupla = tuple(mi_lista)

my_tuple = (35 , 1.79, "Oz" , "Gualla")
my_other_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
print(tupla_empaquetada)
print(lista_a_tupla)

print(my_tuple[0]) # Acceder a elementos
print(my_tuple[-1])
print(my_other_tuple[1:4]) # Crea una nueva tupla con slice
print(len(my_tuple))
print(my_tuple.count("Oz"))
print(my_tuple.index("Gualla"))

new_tuple = my_tuple + my_other_tuple # Concatenar tuplas
print(new_tuple)

if "Yuliana" in lista_a_tupla:
    print("Si")
else:
    print("No")

for i in my_other_tuple:
    print(i)

a,b = (10,20) # Reasignar valores en variables
print(a)
print(b)

# El comodín * crea una lista con los elementos
c,d,*resto = (65,67,45,34,54,56) # Desempaquetar tuplas
print(c)
print(d)
print(resto)

tupla_repetida = (1,2,3,4,5)*3 # Repite la tupla 
print(tupla_repetida)

tupla_1_elemento = (1,) # Si no se le agrega la , es solo un dígito
print(tupla_1_elemento)

sum() # Suma los elementos de una tupla, set o diccionario
