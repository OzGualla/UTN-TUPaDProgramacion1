
n1 = 5
n2 = "2"

try:                                 # A no poder sumar 2 datos distintos
    print(n1 + n2)                   # y encontrar un error
    print("No hay error")            # el Try no se ejecuta 
except:                              # Si hay error se ejecuta el except
    print("Se ah producido una error") 

n2 = 2
try:                           # Si no hay error se ejecuta el bloque de Try
    print(n1 + n2)              # y luego el bloque Else
    print("No hay error")     
except:
    print("Se ah producido una error") 
else:                                            # este bloque se ejecuta si no hay
    print("La ejecucion continua correctamente") # una excepcion
finally:                   #    SE EJECUTA SIEMPRE, HAYA O NO ERROR
    print("Continuar")

n2 = 2  # Captura de excepciones por tipo
try:                                 
    print(n1 + n2)                
    print("No hay error")       
except ValueError:                        
    print("Se ah producido una error de Valor") 
except TypeError:
    print("Se ah producido un error del tipo Dato")

n2 = "2"  
try:                                 
    print(n1 + n2)                
    print("No hay error")       
except ValueError as error:                
    print("Se ah producido una error de Valor") 
    print(error)
except TypeError as error: # Se puede guardar el error dentro de una variable   
    print("Se ah producido un error del tipo Dato")
    print(error)
except Exception as excepcionerror:
    print(excepcionerror)
    
    