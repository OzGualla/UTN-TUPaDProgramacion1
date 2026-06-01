"""Funcion Lambda"""

mascotas = [["Haise",1] , ["Ymir",2] , ["Cosme Fulanito",3] , ["Mandarina",4] , ["Cuthulita",5]]
print(mascotas)

mascotas.sort(key=lambda elemento:elemento[0]) #Parametros y Valor de retorno
print(mascotas) #Acomoda por el indice 0 en esta caso por nombres

mascotas.sort(key=lambda elemento:elemento[1], reverse = True) #Parametros y Valor de retorno
print(mascotas) #Ordena por indice 1 en este caso por numero y reverse = True hace de mayor a menor

