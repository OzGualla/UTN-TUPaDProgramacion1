# ============================================================
# TP2 - Conjuntos y Diagramas de Venn
# Materia: Matemática
# Tecnicatura Universitaria en Programación - Universidad Tecnológica Nacional.
# 
# Este programa permite ingresar los datos de un universo y
# tres conjuntos A, B y C, calcula automáticamente todas las
# regiones del diagrama de Venn y muestra los resultados.
# ============================================================

def separador():

    print("=" * 50)


def validar_numero(mensaje):
    """
    Solicita un string y valida que sea un número entero no negativo.
    Retorna int validado.
    """
    while True:

        num = input(mensaje)

        if not num.isdigit():

            print("Solo se aceptan números enteros no negativos.")

            continue

        return int(num)


def ingreso_dato(mensaje, minimo=0, maximo=None):
    """
    Solicita un número entero al usuario con validación de rango.

    Parámetros:
    mensaje (str): texto a mostrar al usuario
    minimo (int): valor mínimo permitido
    maximo (int): valor máximo permitido (opcional)

    Retorna:
    int: el número ingresado por el usuario
    """
    while True:

        try:

            valor = validar_numero(mensaje)

        except (EOFError, KeyboardInterrupt):

            print("\nEntrada cancelada por el usuario.")

            exit(0)

        except Exception as e:

            print("Ha ocurrido un error inesperado:", type(e).__name__)

            continue   # reiniciar el ciclo, no avanzar a las validaciones

        if valor < minimo:

            print(f"El valor debe ser al menos {minimo}. Intente de nuevo.")

            continue

        if maximo is not None and valor > maximo:

            print(f"El valor no puede superar {maximo}. Intente de nuevo.")
            
            continue

        return valor
        

def main():

    separador()

    print("\n=== CALCULADORA DE CONJUNTOS - DIAGRAMA DE VENN ===\n")

    separador()

    # Ingreso del universo
    print("\n[1] UNIVERSO")

    desc_universo = input("Descripción del universo U: ")

    total_u = ingreso_dato("Número total de elementos de U: ", minimo=1)

    # Nombres de los conjuntos
    print("\n[2] NOMBRES DE LOS CONJUNTOS")

    nombre_a = input("Nombre del conjunto A: ")
    nombre_b = input("Nombre del conjunto B: ")
    nombre_c = input("Nombre del conjunto C: ")

    # Cantidades de cada conjunto
    print("\n[3] CANTIDAD DE ELEMENTOS DE CADA CONJUNTO")

    cant_a = ingreso_dato(f"|{nombre_a}| = ", minimo=0, maximo=total_u)
    cant_b = ingreso_dato(f"|{nombre_b}| = ", minimo=0, maximo=total_u)
    cant_c = ingreso_dato(f"|{nombre_c}| = ", minimo=0, maximo=total_u)

    # Intersecciones entre pares
    print("\n[4] INTERSECCIONES ENTRE PARES DE CONJUNTOS")

    ab = ingreso_dato(f"|{nombre_a} ∩ {nombre_b}| = ", minimo=0, maximo=min(cant_a, cant_b))
    ac = ingreso_dato(f"|{nombre_a} ∩ {nombre_c}| = ", minimo=0, maximo=min(cant_a, cant_c))
    bc = ingreso_dato(f"|{nombre_b} ∩ {nombre_c}| = ", minimo=0, maximo=min(cant_b, cant_c))

    # --- Intersección triple ---
    print("\n[5] INTERSECCIÓN DE LOS TRES CONJUNTOS")

    abc = ingreso_dato(f"|{nombre_a} ∩ {nombre_b} ∩ {nombre_c}| = ", minimo=0, maximo=min(ab, ac, bc))

    # ============================================================
    # CÁLCULOS
    # Fórmula para elementos exclusivos de cada región:
    #   Solo A = |A| - (|A∩B| - |A∩B∩C|) - (|A∩C| - |A∩B∩C|) - |A∩B∩C|
    # ============================================================

    solo_a  = cant_a - (ab - abc) - (ac - abc) - abc
    solo_b  = cant_b - (ab - abc) - (bc - abc) - abc
    solo_c  = cant_c - (ac - abc) - (bc - abc) - abc

    # Elementos en intersecciones de a pares (excluyendo el centro)
    solo_ab = ab - abc
    solo_ac = ac - abc
    solo_bc = bc - abc

    # Principio de Inclusión-Exclusión
    al_menos_uno = cant_a + cant_b + cant_c - ab - ac - bc + abc

    # Elementos fuera de todos los conjuntos
    ninguno = total_u - al_menos_uno


    # ==========
    # RESULTADOS
    # ==========

    print()

    separador()

    print("   RESULTADOS")

    separador()

    print(f"\nUniverso: {desc_universo}")

    print(f"Total de elementos: {total_u}\n")

    print("=== Elementos exclusivos de cada conjunto ===")

    print(f"  Solo {nombre_a}: {solo_a}")
    print(f"  Solo {nombre_b}: {solo_b}")
    print(f"  Solo {nombre_c}: {solo_c}")

    print("\n=== Intersecciones exclusivas (dos conjuntos) ===")

    print(f"  Solo {nombre_a} ∩ {nombre_b}: {solo_ab}")
    print(f"  Solo {nombre_a} ∩ {nombre_c}: {solo_ac}")
    print(f"  Solo {nombre_b} ∩ {nombre_c}: {solo_bc}")

    print("\n=== Intersección de los tres conjuntos ===")

    print(f"  {nombre_a} ∩ {nombre_b} ∩ {nombre_c}:  {abc}")

    print("\n=== Elementos fuera de todos los conjuntos ===")

    print(f"Ninguno de los tres:  {ninguno}")

    print()

    separador()

    # Verificación: suma de todas las regiones debe ser igual a |U|
    total_verificacion = solo_a + solo_b + solo_c + solo_ab + solo_ac + solo_bc + abc + ninguno

    print(f"Verificación (suma de regiones): {total_verificacion}")

    print(f"Total universo: {total_u}")

    if total_verificacion == total_u:

        print("Los datos son consistentes.")

    else:

        print("Atención: los datos ingresados no son consistentes.")

    separador()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
