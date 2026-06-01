""" Inicios en Python """

#esto es un comentario

macho = "Macho Dijo la partera"
name = "BaRo"
lastname = "VeRo"
categoria = "oPeraRio \n\"EspeCiaLizado\""
descripcion = """     aca podes escribir texto largos """
a = 100
b = 10

full_name = f"{name}{lastname}"    #Concatenar correctamente
suma = a + b
resta = a - b
multi = a * b
div = a/b
exponente = a**b
modulo = a%b

print(categoria.capitalize())       #Solo inicial primaria con mayus
print(full_name.upper())            #Letras en mayus
print(full_name.lower())            #Letras en miniscula
print(full_name.capitalize())       #Solo iniciales primarias con mayus
print(full_name.title())            #Iniciales de cada palabra en mayus
print(full_name.swapcase())        #Invierte mayus por minus y viceversa
print(full_name.strip())            #Quita espacios izq y dere
print(full_name.lstrip())           #Quita espacios solo izq
print(full_name.rstrip())           #Quita espacios solo dere
 
print(full_name.find("o"))          #Busca la ubicacion del segmento 
print(full_name.replace("o" , "e")) #Remplaza los atributos

print(len(full_name))               #para saber la longitud de la sentencia
print(full_name[0:4])               #para segmentar la sentencia 

print(suma , multi)                 #Operaciones
print(resta, div)   
print(exponente, modulo)        
print("BaR" in full_name)           # True si encuentra en el atributo de lo contrario False             
print("Ve" not in full_name)        # True si no encuentra en el atributo de lo contrario False
print(descripcion.upper().lstrip())

print(len(macho))
print(macho[0:5], "No" , macho[5:]) # Segmentar sentencia y agregar texto
nuevo_texto = "mAchO dIjO La PartERA"
print(nuevo_texto.splitlines())
print(nuevo_texto)