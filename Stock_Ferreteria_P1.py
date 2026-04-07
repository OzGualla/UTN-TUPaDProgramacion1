
herramientas = []
existencias = []

print("\n---- Sistema de Stock ----")

opcion = ""
while opcion != "8":
    print("1 - Carga inicial de Herramientas\n"\
          "2 - Carga de Existencias\n"\
          "3 - Visualizacion de Inventario\n"\
          "4 - Consulta de Stock\n"\
          "5 - Reporte de Agotados\n"\
          "6 - Alta de Nuevo Producto\n"\
          "7 - Actualizacion de Stock\n"\
          "8 - Salir")
    opcion = input("-> ")
    while not opcion.isdigit():
        print("\nOpcion Invalida")
        print("1 - Carga inicial de Herramientas\n"\
          "2 - Carga de Existencias\n"\
          "3 - Visualizacion de Inventario\n"\
          "4 - Consulta de Stock\n"\
          "5 - Reporte de Agotados\n"\
          "6 - Alta de Nuevo Producto\n"\
          "7 - Actualizacion de Stock\n"\
          "8 - Salir")
        opcion = input("-> ")

    if opcion == "1":
        cant_herramientas = input("Ingrese cantidad de herramientas a registrar: ")
        while not cant_herramientas.isdigit():
            print("Ingrese numero valido")
            cant_herramientas = input("Ingrese cantidad de herramientas a registrar: ")
        cant_herramientas = int(cant_herramientas)
        for i in range(cant_herramientas+1):
            herramienta_ingresada = input(f"Ingrese nombre de herramienta n°{i+1}: ")
            while not herramienta_ingresada.isalpha():
                print("nombre no valido, solo se aceptan letras")
                herramienta_ingresada = input(f"Ingrese nombre de herramienta n°{i+1}: ")
    elif opcion == "8":
        print("Sistema Cerrado")
        break
    else:
        print("\nOpcion invalida")    