""" Tp3- Repetitivas"""
print("\n------- Bienvenido al TP3 - Repetitivas -------\n")
print("")

opcion = ""
# Me decidi por el Match case por necesidad de prolijidad y no entregar mas de 1 archivo.py
while True:
    print("-"*65)
    print("1 - Caja de Kiosco\n"\
      "2 - Acceso al Campus y Menú Seguro\n"\
      "3 - Agenda de Turnos con nombres\n"\
      "4 - Escape Room: La Bóveda\n"\
      "5 - Escape Room: La Arena del Gladiador\n"\
      "6 - Salir")
    opcion = input("\nElija un ejercicio: ")
    match opcion:
        case "1":
            # Ejercicio 1 "Caja de Kiosco"
            nombre = input("Ingrese su nombre de cliente: ")
            # Validar nombre
            while not nombre.isalpha():
                nombre = input("Ingrese su nombre de cliente: ")

            cant_producto = input("Ingrese cantidad de productos deseados: ")
            # Validar cantidad de productos, evitando cantidad 0
            while not cant_producto.isdigit() or cant_producto == "0":
                cant_producto = input("Ingrese cantidad de productos: ")
            cant_producto = int(cant_producto)
            # Declare varias variables para ir sumando y reasignando los valores
            precio = 0
            precio_con_descuento = 0
            precio_total_con_descuento = 0
            precio_total = 0
            ahorro = 0
            ahorro_total = 0
            promedio_de_precios = 0
            datos_finales = ""
            # Declaracion de Float
            promedio_de_precios = float(promedio_de_precios)

            for i in range(1,cant_producto+1):
                precio = input(f"Ingrese precio {i}: $")
                while not precio.isdigit():
                    print("Solo se aceptan numeros enteros")
                    precio = input(f"Ingrese precio {i}: $")
                precio = int(precio)
                precio_total += precio 

                descuento = input("Tiene descuento S/N: ")
                # Validacion de S/N
                while not (descuento.lower() == "s") and not (descuento.lower() == "n"):
                    descuento = input("Tiene descuento S/N: ")
                if descuento.lower() == "s":
                    ahorro = (precio/100) * 10
                precio_con_descuento = precio - ahorro
                ahorro_total += ahorro
                precio_total_con_descuento += precio_con_descuento
                # Al no poder acceder a la informacion del for, decidi concatenar un string
                # Cada vez que se ejecuta 1 ciclo, la informacion vieja queda guardada en esta variable,
                # Y se le concatena el nuevo string. luego lo imprimo al finalizar la ejecucion
                datos_finales += f"Producto {i} - Precio: {precio} - Descuento (S/N): {descuento.upper()}\n"
            # promedio de precios
            promedio_de_precios = precio_total_con_descuento / cant_producto

            print(f"\nCliente: {nombre.capitalize()}\nCantidad de productos: {cant_producto}\n")
            print(datos_finales)
            print(f"\nTotal sin descuentos: ${precio_total:.0f}\n"\
                f"Total con descuentos: ${precio_total_con_descuento:.0f}\n"\
                f"Ahorro: ${ahorro}\n"\
                f"Promedio por producto: ${promedio_de_precios:.2f}")

# ----------------------------------------------------------------------------------------------------

    # Ejercicio 2 "Acceso al Campus y Menú Seguro"
        case "2":
            usuario_correcto = "usuario"
            clave_correcta = "python123"
            user = input("\nIngrese su usuario: ")
            password = input("Ingrese su clave: ")
            count = 0
            # Doble validacion , usuario y clave
            while not user == usuario_correcto or not password == clave_correcta:
                count += 1
                print(f"\nIntento {count}/3 - Usuario: {user}")
                print(f"Clave: {password}")
                print("Error: Credenciales Invalidas")
                if count < 3:
                    user = input("\nIngrese su usuario: ")
                    password = input("Ingrese su clave: ")
                if count == 3:
                    print("Cuenta bloqueada")
                    break

            if count < 3:
                print("\n--- Acceso Concedido ---\n")
                opcion = ""
                while opcion != "4":
                    print("1 - Ver estado de inscrpcion")
                    print("2 - Cambiar Clave")
                    print("3 - Mostrar mensaje motivacional")
                    print("4 - Salir")
                    opcion = input("-> ")
                    # Primero verifico que el input no sea letras ni caracteres especiales
                    if opcion.isalpha() or not opcion.isalnum():
                        print("Error: Ingrese un numero valido")
                    # Luego verifico que el input sea alphanumerico
                    while opcion.isdigit():
                        if opcion == "1":
                            print("\nEstado: Inscripto\n")
                            break
                        elif opcion == "2":
                            new_password = input("\nIngrese nueva clave (Minimo 6 caracteres): ")
                            # Si la nueva clave es menor a 6, no espera a que ingreses la verificacion de esta
                            if len(new_password) < 6:
                                print("\nError: La clave debe tener minimo 6 caracteres\nintente nuevamente")
                                break
                            new_password_confirm = input("Confirme su clave: ")
                            if new_password == new_password_confirm:
                                print("\nSu clave a sido cambiada con exito\n")
                                break
                            else:
                                print("\nError: Las claves no coinciden\nIntente nuevamente")
                                break
                        elif opcion == "3":
                            print("\nMensaje: No esta muerto lo que yace eternamente.\nY con el paso de los Evos, Incluso la muerte puede morir...\n")
                            break
                        elif opcion == "4":
                            print("Salir")
                            break
                        else: # Si el alphanumerico esta fuera de rango, no acepta el input
                            print("\nError: Opcion Invalida, fuera de rango\n")
                            break

#------------------------------------------------------------------------------------------------------

    # Ejercicio 3 "Agenda de Turnos con nombres"
        case "3":
            print("\n-- Bienvenido --")
            nombre_paciente = "libre"
            turno_disponible_lunes = 4
            turno_disponible_martes = 3
            turno_lunes1 = "Libre"
            turno_lunes2 = "Libre"
            turno_lunes3 = "Libre"
            turno_lunes4 = "Libre"
            turno_martes1 = "Libre"
            turno_martes2 = "Libre"
            turno_martes3 = "Libre"
            cantidad_turnos_ocupados_lunes = 0
            cantidad_turnos_ocupados_martes = 0
            turnos_cancelados_lunes = 0
            turnos_cancelados_martes = 0

            nombre_operador = input("Ingrese nombre operador: ")
            # Verificar nombre del operador
            while not nombre_operador.isalpha():
                print("Error: Solo se aceptan letras")
                nombre_operador = input("Ingrese nombrne operador: ")
                print(f"\nBienvenido {nombre_operador.capitalize()}")
            opcion = ""

            # Menu repetitivo
            while opcion != 5:
                opcion = input("Menu:\n1 - Reservar Turno\n"\
                            "2 - Cancelar Turno\n3 - Ver agenda del dia\n"\
                            "4 - Ver resumen General\n5 - Cerrar Sistema\n-> ")
                # Asignar turnos
                if opcion == "1":
                    dia = input(f"\nSelecione dia del turno:\n"\
                                f"1 - Lunes, Turnos disponibles: {turno_disponible_lunes}\n"\
                                f"2 - Martes, Turnos disponibles: {turno_disponible_martes}\n-> ")
                    # Turnos Lunes
                    if dia == "1":
                        nombre_paciente = input("Lunes:\nIngrese nombre de paciente: ")
                        while not nombre_paciente.isalpha():
                            print("Error: Solo se aceptan letras")
                            nombre_paciente = input("Lunes:\nIngrese nombre de paciente: ")
                        if nombre_paciente in (turno_lunes1,turno_lunes2,turno_lunes3,turno_lunes4):
                            print("- Paciente ya ingresado -\n")
                        elif turno_lunes1 == "Libre":
                            turno_lunes1 = nombre_paciente
                            turno_disponible_lunes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Lunes 1:   {turno_lunes1.capitalize()}\n")
                        elif turno_lunes2 == "Libre":
                            turno_lunes2 = nombre_paciente
                            turno_disponible_lunes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Lunes 1:   {turno_lunes1.capitalize()}")
                            print(f"Lunes 2:   {turno_lunes2.capitalize()}\n")
                        elif turno_lunes3 == "Libre":
                            turno_lunes3 = nombre_paciente
                            turno_disponible_lunes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Lunes 1:   {turno_lunes1.capitalize()}")
                            print(f"Lunes 2:   {turno_lunes2.capitalize()}")
                            print(f"Lunes 3:   {turno_lunes3.capitalize()}\n")
                        elif turno_lunes4 == "Libre":
                            turno_lunes4 = nombre_paciente
                            turno_disponible_lunes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Lunes 1:   {turno_lunes1.capitalize()}")
                            print(f"Lunes 2:   {turno_lunes2.capitalize()}")
                            print(f"Lunes 3:   {turno_lunes3.capitalize()}")
                            print(f"Lunes 4:   {turno_lunes4.capitalize()}\n")
                        cantidad_turnos_ocupados_lunes += 1
                    # Turnos Martes
                    elif dia == "2":
                        nombre_paciente = input("Martes:\nIngrese nombre de paciente: ")
                        while not nombre_paciente.isalpha():
                            print("Error: Solo se aceptan letras")
                            nombre_paciente = input("Martes:\nIngrese nombre de paciente: ")
                        if nombre_paciente in (turno_martes1,turno_martes2,turno_martes3):
                            print("Paciente ya ingresado")
                        elif turno_martes1 == "Libre":
                            turno_martes1 = nombre_paciente
                            turno_disponible_martes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Martes 1:   {turno_martes1.capitalize()}\n")
                        elif turno_martes2 == "Libre":
                            turno_martes2 = nombre_paciente
                            turno_disponible_martes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Martes 1:   {turno_martes1.capitalize()}")
                            print(f"Martes 2:   {turno_martes2.capitalize()}\n")
                        elif turno_martes3 == "Libre":
                            turno_martes3 = nombre_paciente
                            turno_disponible_martes -= 1
                            print(f"\nDia Turno: Paciente -\n"\
                                f"Martes 1:   {turno_martes1.capitalize()}")
                            print(f"Martes 2:   {turno_martes2.capitalize()}")
                            print(f"Martes 3:   {turno_martes3.capitalize()}\n")
                        cantidad_turnos_ocupados_martes += 1

                # Cancelar Turnos
                if opcion == "2":
                    print("-- Cancelar Turnos --")
                    dia = input("Selecione dia\n"\
                                f"1 - Lunes: Turnos disponibles: {turno_disponible_lunes}\n"\
                                f"2 - Martes: Turnos disponibles: {turno_disponible_martes}\n-> ")
                    if dia == "1": # Cacelar lunes
                        print(f"\nDia Turno: Paciente -\n"\
                            f"Lunes 1:   {turno_lunes1.capitalize()}")
                        print(f"Lunes 2:   {turno_lunes2.capitalize()}")
                        print(f"Lunes 3:   {turno_lunes3.capitalize()}")
                        print(f"Lunes 4:   {turno_lunes4.capitalize()}\n")
                        nombre_paciente = input("Ingrese nombre del paciente a cancelar: ")
                        if nombre_paciente == turno_lunes1:
                            turno_lunes1 = "Libre"
                        elif nombre_paciente == turno_lunes2:
                            turno_lunes2 = "Libre"
                        elif nombre_paciente == turno_lunes3:
                            turno_lunes3 = "Libre"
                        elif nombre_paciente == turno_lunes4:
                            turno_lunes4 = "Libre"
                        turno_disponible_lunes += 1
                        turnos_cancelados_lunes += 1
                    elif dia == "2": # Cancelar martes
                        print(f"\nDia Turno: Paciente -\n"\
                            f"Martes 1:   {turno_martes1.capitalize()}")
                        print(f"Martes 2:   {turno_martes2.capitalize()}")
                        print(f"Martes 3:   {turno_martes3.capitalize()}\n")
                        nombre_paciente = input("Ingrese nombre del turno a cancelar: ")
                        if nombre_paciente == turno_martes1:
                            turno_martes1 = "Libre"
                        elif nombre_paciente == turno_martes2:
                            turno_martes2 = "Libre"
                        elif nombre_paciente == turno_martes3:
                            turno_martes3 = "Libre"
                        turno_disponible_martes += 1
                        turnos_cancelados_martes += 1

                # Mostrar agenda completa
                if opcion == "3":
                    print(f"\nDia Turno: Paciente -\n"\
                            f"Lunes 1:   {turno_lunes1.capitalize()}")
                    print(f"Lunes 2:   {turno_lunes2.capitalize()}")
                    print(f"Lunes 3:   {turno_lunes3.capitalize()}")
                    print(f"Lunes 4:   {turno_lunes4.capitalize()}")
                    print(f"\nDia Turno: Paciente -\n"\
                            f"Martes 1:  {turno_martes1.capitalize()}")
                    print(f"Martes 2:  {turno_martes2.capitalize()}")
                    print(f"Martes 3:  {turno_martes3.capitalize()}\n")

                # Resumen general
                if opcion == "4":
                    if cantidad_turnos_ocupados_lunes > cantidad_turnos_ocupados_martes:
                        print(f"\nDia con mayor cantidad de Turnos asignados: Lunes\n"\
                            f"Lunes  - Se asignaron: {cantidad_turnos_ocupados_lunes}\n"\
                            f"Martes - Se asignaron: {cantidad_turnos_ocupados_martes}")
                    elif cantidad_turnos_ocupados_lunes < cantidad_turnos_ocupados_martes:
                        print(f"\nDia con mayor cantidad de Turnos asignados: Martes\n"\
                            f"Martes - Se asignaron: {cantidad_turnos_ocupados_martes}\n"\
                            f"Lunes  - Se asignaron: {cantidad_turnos_ocupados_lunes}")
                    else:
                        print(f"\nDia con mayor cantidad de Turnos asignados: Empate\n"\
                            f"Lunes  - Se asignaron: {cantidad_turnos_ocupados_lunes}\n"\
                            f"Martes - Se asignaron: {cantidad_turnos_ocupados_martes}")
                    print(f"Cantidad total de turnos asignados: {cantidad_turnos_ocupados_lunes + cantidad_turnos_ocupados_martes}")
                    print(f"Cantidad total de turnos cancelados: {turnos_cancelados_lunes + turnos_cancelados_martes}")

                # Cerrar sistema
                if opcion == "5":
                    print("Sistema Cerrado")
                    break

# ------------------------------------------------------------------------------------------------------

    # Ejercicio 4 "Escape Room: La Bóveda"
        case "4":
            import random
            import string
            # Declaracion de estado
            energia = 100
            tiempo = 12
            cerraduras_abiertas = 0
            alarma = False
            codigo_parcial = ""
            forzar_seguidas = 0
            hackear_seguidas = 0

            print("Comando Central: Cual es su nombre Agente?")
            agente = input("-> ")
            # Validacion de nombre
            while not agente.isalpha():
                print("Comando Central: Vamos apresurate, no hay tiempo que perder...\n"
                    "solo acepto letras, cual es tu nombre?")
                agente = input("-> ")
            # Mensaje de Bienvenida
            print(f"\nComando Central: Bienvenido, Agente {agente.capitalize()}.\nTu mision es abrir esta bóveda sellada por tres cerraduras.\n"\
                "Tu objetivo sera abrirlas todas antes de que tus recursos se agoten.\n"\
                "Disponés de una cantidad limitada de energía y tiempo,\n"\
                "y cada decisión que tomes será crucial.\n"\
                "Si lográs abrir sus tres sellos antes de quedarte sin energía o sin tiempo…\n"\
                "la victoria será tuya.\n"\
                "Pero no te confies, si se activa la alarma, todo abra terminado...\n"\
                "Buena Suerte Agente...\n")
            # Mensaje Alarma == True
            mensaje_dispara_alarma = (f"\n--- ALERTA: SISTEMA BLOQUEADO ---\nComando Central: La alarma ha sido activada, Agente {agente.capitalize()}!\n"\
                                "Las luces de emergencia bañan la bóveda en rojo y las salidas están siendo selladas.\n"\
                                "Fuerzas de seguridad convergen rápidamente sobre tu posición\n"\
                                "Comando Central: La misión ha fracasado. Retirada inmediata… si aún es posible.")

            # Condiciones del juego y estados del agente
            while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
                if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
                    print(mensaje_dispara_alarma)
                    break
                if alarma == True:
                    estado_alarma = "On"
                if alarma == False:
                    estado_alarma = "Off"
                print("-"*26)
                print("| Tu estado actual:\n"\
                    f"| Energia = {energia}\n"\
                    f"| Tiempo = {tiempo}\n"\
                    f"| Cerraduras abiertas = {cerraduras_abiertas}\n"\
                    f"| Alarma = {estado_alarma}")
                print("-"*26)
                print("\nComando Central: Cual sera tu proximo movimiento Agente?\n"\
                    "1 - Forzar Cerradura (Energia: -20 , Tiempo: -2)\n"\
                    "2 - Hackear panel (Energia: -10, Tiempo: -3)\n"\
                    "3 - Descansar (Energia +15, Tiempo -1 (Si la Alarma esta 'On' , perderas 10 de energia extra!))")
                opcion = input("\n-> ")
                # Validacion de opciones
                while not opcion.isdigit():
                    print("Comando Central: Cuidado Agente, Solo puedes utilizar numeros y solo puedes seleccionar entre las opciones disponibles!")
                    opcion = input("Cual sera tu proximo movimiento?\n-> ")
                # Estructura del juego
                # Forzar Cerraduras
                if opcion == "1":
                    energia -= 20
                    tiempo -= 2
                    forzar_seguidas += 1
                    hackear_seguidas -= 1
                    if forzar_seguidas == 2:
                        print("-"*65)
                        print("Comando Central: Cuidado! Estas forzando demaciado la cerradura Agente! No aguantara tantos intentos seguidos!")
                    if forzar_seguidas == 3:
                        alarma = True
                        cerraduras_abiertas -= 1
                        print("-"*65)
                        print("La cerradura se Trabo por intentar forzarla demaciadas veces seguidas...")
                        print("Comando Central: Deprisa Agente! Se ah activado la Alarma!)")
                    if energia < 40:
                        print("Comando Central: Cuidado Agente! Se esta por activar la alarma!\n"\
                            "Debes arriesgarte y cortar uno de los 3 cables!\n"\
                            "Solo tendras 1 oportunidad!")
                        numero_activa_alarma = random.randint(1,3)
                        numero_activa_alarma = str(numero_activa_alarma)
                        print(numero_activa_alarma)
                        print("Comando Central: Es imposible saber que cable la activara...\n"\
                            "Tendras que decidir...\n")
                        print("1 - Cable Rojo\n2 - Cable Verde\n3 - Cable Azul")
                        cable_alarma = input("-> ")
                        if cable_alarma == numero_activa_alarma:
                            alarma = True
                            print("El cable cortado ah disparado el sistema de seguridad!")
                            print("Comando Central: Deprisa Agente! Se ah activado la Alarma!)")
                            print(mensaje_dispara_alarma)
                        else:
                            print("-"*65)
                            print("Has cortado el cable correcto, logras abrir una cerradura!\n"\
                                "Y has desactivar la Alarma!")
                            alarma == False
                            cerraduras_abiertas += 1
                    else:
                        cerraduras_abiertas += 1
                        print("-"*65)
                        print("Con movimientos precisos de tu ganzua, logras abrir una cerradura")
                        print(f"Cerraduras abiertas: {cerraduras_abiertas}/3\n")

                # Hackear panel
                elif opcion == "2":
                    # Me tome la libertad de usar el mismo concepto que Forzar_Seguidas, solo para aumentar un poco la dificultad
                    # Ya que si intentas hackear el panel 3 veces, se te terminara el tiempo
                    hackear_seguidas += 1
                    forzar_seguidas -= 1
                    energia -= 10
                    tiempo -= 3
                    if hackear_seguidas == 2:
                        print("Comando Central: Cuidado Agente! Si el sistema te detecta, Activara la alarma!")
                    if hackear_seguidas == 3:
                        print("Comando Central: El sistema te ah detectado y ah activado la alarma Agente!")
                        alarma = True
                        cerraduras_abiertas -= 1
                    """La consigna me a parecido ambigua y no la termino de entender bien.

                        --- Debe usar un for de 4 pasos mostrando progreso.
                        En cada paso sumar una letra al codigo_parcial (por ejemplo A).
                        Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura ---

                        Decidi sumar 2 caracteres en lugar de 1, en cada iteracion para poder lograr la consigna """
                    print("-"*65)
                    print("--- Iniciando Hackeo de Panel ---")
                    for i in range(4):
                        # Implemente un random de caracteres, para que la 'clave' a descifrar, parezca mas realista
                        codigo_parcial += random.choice(string.ascii_uppercase)
                        codigo_parcial += random.choice(string.ascii_uppercase)
                        print("Descifrando codigo...")
                        print(f"{codigo_parcial}...")
                        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                            codigo_parcial = ""
                            cerraduras_abiertas += 1
                            print("Has conseguido Hackear el Sistema!\n"\
                                "Se ah abierto una cerradura\n"\
                                f"Cerraduras abiertas: {cerraduras_abiertas}")
                
                # Descansar
                elif opcion == "3":
                    print("Comando Central: Tomate un respiro Agente, Tu puedes lograrlo!")
                    energia += 15
                    if energia > 100:
                        energia = 100
                    tiempo -= 1
                    if alarma == True:
                        energia -= 10

                # Por si el usuario ingresa un valor fuera del rango de opciones
                else:
                    print("*"*65)
                    print("Comando Central: Opcion invalida, Intenta denuevo")

                            
            if cerraduras_abiertas == 3:
                print("-"*65)
                print("Lograste abrir la boveda!\n"\
                    f"Has cumplido tu mision Agente {agente.capitalize()}!")
            if energia <= 0 or tiempo <= 0:
                print("-"*65)
                print(mensaje_dispara_alarma)

# -------------------------------------------------------------------------------------------------------

     # Ejercicio 5 "“Escape Room:"La Arena del Gladiador""
        case "5":
            # Declaracion de variables
            vida_gladiador = 100
            vida_enemigo = 100
            pociones_vida = 3
            danio_base = 15
            danio_base_enemigo = 12
            turno_gladiador = True

            print("--- Bianvenido a la Arena! ---")
            nombre_gladiador = input("Ingresa el nombre de tu gladiador: ")
            # Validacion de nombre
            while not nombre_gladiador.isalpha():
                print("Error: Solo se permiten letras")
                nombre_gladiador = input("Ingresa el nombre de tu gladiador: ")

            # Condicion para finalizar la ejecucion
            while vida_gladiador > 0 and vida_enemigo > 0:
                print("\n--- INICIO DEL COMBATE ---\n"\
                    f"{nombre_gladiador.capitalize()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
                opcion = ""
                # Mientras Turno Gladiador sea True, se ejecuta este bloque
                while turno_gladiador == True:
                    print("Elije tu accion:\n"\
                        "1 - Ataque Pesado\n2 - Rafaga Veloz\n3 - Curar")
                    opcion = input("-> ")
                    while not opcion.isdigit():
                        print("Solo se aceptan numeros")
                        opcion = input("-> ")
                    if opcion == "1":
                        # Multiplicador de golpe
                        if vida_enemigo < 20:
                            golpe_critico = danio_base * 1.5
                            vida_enemigo -= golpe_critico
                            print(f"Golpe Critico: ¡Atacaste al enemigo por {golpe_critico} puntos de daño!")
                            turno_gladiador = False
                            break
                        # Ataque normal
                        else:
                            vida_enemigo -= danio_base
                            print(f"Le hiciste {danio_base} punto de daño al enemigo")
                            turno_gladiador = False
                            break

                    if opcion == "2":
                        # Ataque de rafaga con ciclo For
                        for i in range(3):
                            vida_enemigo -= 5
                            print(" > Golpe conectado por 5 de daño")
                        turno_gladiador = False

                        # Beber pocion de vida
                    if opcion == "3":
                        if pociones_vida > 0:
                            vida_gladiador += 30
                            pociones_vida -= 1
                            print("Bebes una pocion\nTe has curado 30 puntos de vida")
                            turno_gladiador = False
                            break
                        else: # si pociones >= 0, el jugador pierde el turno y no se cura
                            print("¡No quedan pociones! y pierdes el turno")
                            turno_gladiador = False
                            break
                    else:
                        print("Opcion invalida, vuelve a elegir")
                # Si turno gladiador False
                if turno_gladiador == False:
                    print("Turno Enemigo!")
                    print("¡El enemigo te atacó por 12 puntos de daño!")
                    vida_gladiador -= danio_base_enemigo
                    # al volver a cambiar esta variable, se ejecuta el ciclo nuevamente
                    turno_gladiador = True
            # Condiciones de victoria
            if vida_gladiador > 0:
                print(f"\n¡VICTORIA! {nombre_gladiador.capitalize()} ha ganado la batalla.")
            elif vida_gladiador <=0:
                print("\nDERROTA. Has caído en combate.")
# -------------------------------------------------------------------------------------------------------
        # Salir del programa
        case "6":
            print("Gracias por su tiempo, espero les haya gustado!")
            break
        # Opcion invalida inicio
        case _:
            print("Opcion Invalida, porfavor, elije denuevo")
            continue