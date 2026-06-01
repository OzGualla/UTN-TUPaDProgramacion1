
# Ordenamiento Burbuja
# Lista Desordenada
mi_lista = [1000,3124,3654,124,134,123,235,346,457,576,3426,234,165]

# Se define la cantidad de elementos de la lista
cantidad_elementos = len(mi_lista)
print("Lista original:")
print(mi_lista)
# Se recorre con un for anidado
# Usando la cantidad de elementos - 1 ya que el ultimo numero no lo va a comparar
for indice_pasada in range(cantidad_elementos -1):
    # Verificar cuantos bucles hace el codigo
    print("Recorrido : ",indice_pasada+1)
    # Bandera
    hizo_intercambio = False
    # La cantidad de recorrido se va reduciendo en 1
    for indice_actual in range(cantidad_elementos -1 -indice_pasada):
        if mi_lista[indice_actual] > mi_lista[indice_actual +1]:
            # Si el numero siguiente es mayor, se cambia el orden de estos
            mi_lista[indice_actual],mi_lista[indice_actual +1] = mi_lista[indice_actual +1],mi_lista[indice_actual]
            # Y cambia la bandera a True, afirmando que hubo cambios de variables
            hizo_intercambio = True
    # Si no se registraron cambios, osea la lista ya estaba ordenada, se termina la ejecucion en el primer buble
    if hizo_intercambio == False:
        break
# Lista Ordenada
print("Lista ordenada:")
print(mi_lista)

# Busqueda Binaria

buscar_numero = int(input("Buscar numero: "))
indice_inicial = 0
indice_final = len(mi_lista)-1
indice_encontrado = -1

while (indice_inicial <= indice_final) and indice_encontrado == -1:
    indice_medio = (indice_inicial + indice_final) // 2
    if mi_lista[indice_medio] == buscar_numero:
        indice_encontrado = indice_medio
    else:
        if mi_lista[indice_medio] < buscar_numero:
            indice_inicial = indice_medio + 1
        else:
            indice_final = indice_medio - 1
print()

if indice_encontrado == -1:
    print("Numero no encontrado")
else:
    print(f"Numero encontrado: {buscar_numero} en la posicion: {indice_encontrado}")
print()
