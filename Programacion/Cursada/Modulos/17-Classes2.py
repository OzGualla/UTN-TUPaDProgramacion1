""" Mas Clases """

class MyCar:
    def __init__(self, marca, linea = "Base", modelo = "Indefinido"):
        self.marca = marca
        self.marca = modelo
        self.linea = linea
        self.mensaje = (f"Su vehiculo {marca} {linea} {modelo} esta listo")

    
    def engine(self):
        encendido = input("Encender Motor? (Y/N) =  ")
        if encendido.lower() == "y" or encendido.lower() == "yes":
            print("Puede conducir") 
        elif encendido.lower() == "n" or encendido.lower() == "no":
            print("No puede conducir")
        else:
            print("Ingrese opcion valida")
            
marca = input("Ingrese la marca de su vehiculo o salir: ")
if marca.lower() == "salir":
    print("Sin vehiculo")
linea = input("Ingrese la linea de su vehiculo: ")
modelo = input("Ingrese el modelo de su vehiculo: ")
if modelo == "":
    print("No se ah registrado un modelo, Intente denuevo")

my_palio = MyCar(marca, linea, modelo)
print(my_palio.mensaje)

my_palio.engine()

