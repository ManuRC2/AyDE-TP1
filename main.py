# estudiante1_email: str
# estudiante1_contraseña: str
# estudiante1_nombre: str
# estudiante1_hobbies: str
# estudiante1_nacimiento: str
# estudiante1_biografia: str
# estudiante1_me_gusta: str
# estudiante2_email: str
# estudiante2_contraseña: str
# estudiante2_nombre: str
# estudiante2_hobbies: str
# estudiante2_nacimiento: str
# estudiante2_biografia: str
# estudiante2_me_gusta: str
# estudiante3_email: str
# estudiante3_contraseña: str
# estudiante3_nombre: str
# estudiante3_hobbies: str
# estudiante3_nacimiento: str
# estudiante3_biografia: str
# estudiante3_me_gusta: str
# usuario_log: str
# menu: str
# submenu: str
# submenu_2: str

from getpass import getpass
from datetime import datetime
import os

################ FUNCIONES ################

"""
funcion para limpiar consola
"""
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

"""
esperar input del usuario para continuar
"""
def esperar_input():
    # uso getpass para que no se vean los caracteres que se ingresan
    getpass("\nPresione enter para continuar...")

"""
calcula la edad de una persona dada su fecha de nacimiento en formato (AAAA-MM-DD)

fecha_actual = date
año_nac, mes_nac, dia_nac, año_actual, mes_actual, dia_actual: int

"""
def calcular_edad(fecha_nacimiento: str):
    if not fecha_nacimiento:
        return ""
    fecha_actual = datetime.today()
    año_nac = int(fecha_nacimiento[:4])
    mes_nac = int(fecha_nacimiento[5:7])
    dia_nac = int(fecha_nacimiento[8:10])
    año_actual = int(fecha_actual.strftime("%Y"))
    mes_actual = int(fecha_actual.strftime("%m"))
    dia_actual = int(fecha_actual.strftime("%d"))
    
    edad = año_actual - año_nac

    if not mes_actual >= mes_nac and not dia_actual >= dia_nac:
        edad -= 1

    return edad

"""
funcion de logueo, 3 intentos para ingresar

intentos: int
logueado, email: str
"""
def ingresar():
    intentos = 3
    logueado = ""
    email = ""
    while intentos > 0 and not logueado:
        email = input("Ingrese su email: ")
        if email == estudiante1_email:
            contraseña = getpass(f"Ingrese la contraseña para {email}: ")
            if contraseña == estudiante1_contraseña:
                logueado = estudiante1_email
            else: 
                intentos = intentos - 1
                print(f"Contraseña incorrecta. {intentos} intentos restantes.")
                esperar_input()

        elif email == estudiante2_email:
            contraseña = getpass(f"Ingrese la contraseña para {email}: ")
            if contraseña == estudiante2_contraseña:
                logueado = estudiante2_email 
            else: 
                intentos = intentos - 1
                print(f"Contraseña incorrecta. {intentos} intentos restantes.")
                esperar_input()
        
        elif email == estudiante3_email:
            contraseña = getpass(f"Ingrese la contraseña para {email}: ")
            if contraseña == estudiante3_contraseña:
                logueado = estudiante3_email 
            else: 
                intentos = intentos - 1
                print(f"Contraseña incorrecta. {intentos} intentos restantes.")
                esperar_input()
        
        else:
            intentos = intentos - 1
            print(f"Email inválido. {intentos} intentos restantes.")
            esperar_input()
        clear()
    return logueado

"""
imprime el menú si es necesario, y devuelve el valor del menu al que se tiene que entrar
"""
def ingresar_menu(menu: str):
    clear()

    if menu != "":
        return menu
    
    print("\nBienvenido, ¿Que desea hacer?")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")  
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir\n")
    menu = input("Ingrese una opción: ")

    clear()

    return menu

""" 
funcion que parsea la entrada de las fechas de nacimiento

fecha_parseada, entrada: str
"""
def ingresar_fecha_nacimiento():
    fecha_parseada = ""
    while not fecha_parseada:
        entrada = input("Ingrese su fecha de nacimento (AAAA-MM-DD): ")
        try:
            fecha_parseada = datetime.strptime(entrada, "%Y-%m-%d")
        except Exception as e:
            clear()
            print("Por favor, verifique que el formato de la fecha ingresada sea correcto.\n")
    # se devuelve el string de entradda, y no la fecha parseada en formato Datetime, porque asi es indicado en el enunciado
    return entrada

""" 
funcion que imprime el menú para editar datos personales, con los datos especificados del estudiante

opcion: int
"""
def menu_editar_datos_personales(nacimiento: str, biografia: str, hobbies: str):
    print(nacimiento, biografia, hobbies)
    print("\na. Editar datos personales\n")
    print(f"1. Fecha de Nacimiento (actual: {nacimiento}): ")
    print(f"2. Biografia (actual: {biografia}): ")
    print(f"3. Hobbies (actual: {hobbies}): ")
    print(f"0. Volver\n")

    opcion = input("Ingrese una opción: ")
    clear()
    return opcion

""" 
muestra los datos brindados de un estudiante
"""
def mostrar_datos_estudiante(nombre: str, fecha_nacimiento: str, biografia: str, hobbies: str):
    print(f"\nNombre: {nombre}")
    print(f"Fecha de nacimiento: {fecha_nacimiento}")
    print(f"Edad: {calcular_edad(fecha_nacimiento)}")
    print(f"Biografía: {biografia}")
    print(f"Hobbies: {hobbies}")

################ VARIABLES ################

estudiante1_email: str = "estudiante1@ayed.com"
estudiante1_contraseña: str = "111222"
estudiante1_nombre: str = "Estudiante1"
estudiante1_hobbies: str = ""
estudiante1_nacimiento: str = ""
estudiante1_biografia: str = ""
estudiante1_me_gusta: str = ""

estudiante2_email: str = "estudiante2@ayed.com"
estudiante2_contraseña: str = "333444"
estudiante2_nombre: str = "Estudiante2"
estudiante2_hobbies: str = ""
estudiante2_nacimiento: str = ""
estudiante2_biografia: str = ""
estudiante2_me_gusta: str = ""

estudiante3_email: str = "estudiante3@ayed.com" 
estudiante3_contraseña: str = "555666"
estudiante3_nombre: str = "Estudiante3"
estudiante3_hobbies: str = ""
estudiante3_nacimiento: str = ""
estudiante3_biografia: str = ""
estudiante3_me_gusta: str = ""

usuario_log: str = ""

menu: str = ""
submenu: str = ""
submenu_2: str = ""

usuario_log = ingresar()

if usuario_log:
    print("Acceso correcto! Ingresando al programa...")
else:
    print("Acceso invalido. Saliendo del programa...")
    menu = "0"
esperar_input()

## menu interactivo ##
while menu != "0":
    menu = ingresar_menu(menu)
    match menu:
        case "1":
            ## opción 1. gestionar mi perfil ##
            clear()
            if submenu == "":
                print("\nGestión de Perfil.")
                print("\na. Editar mis datos personales")
                print("b. Eliminar mi perfil")
                print("c. Volver\n")
                submenu = input("Ingrese una opción: ")
                clear()
            match submenu.lower():
                case "a":
                    if usuario_log == estudiante1_email:
                        modificacion = menu_editar_datos_personales(estudiante1_nacimiento, estudiante1_biografia, estudiante1_hobbies)
                        match modificacion:
                            case "1":
                                estudiante1_nacimiento = ingresar_fecha_nacimiento()
                            case "2":
                                dato = input("Ingrese su biografía: ")
                                estudiante1_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante1_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")
                                esperar_input()

                    if usuario_log == estudiante2_email:
                        modificacion = menu_editar_datos_personales(estudiante2_nacimiento, estudiante2_biografia, estudiante2_hobbies)
                        match modificacion:
                            case "1":
                                estudiante2_nacimiento = ingresar_fecha_nacimiento()
                            case "2":
                                dato = input("Ingrese su biografía: ")
                                estudiante2_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante2_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")
                                esperar_input()

                    if usuario_log == estudiante3_email:
                        modificacion = menu_editar_datos_personales(estudiante3_nacimiento, estudiante3_biografia, estudiante3_hobbies)
                        match modificacion:
                            case "1":
                                estudiante3_nacimiento = ingresar_fecha_nacimiento()
                            case "2":
                                dato = input("Ingrese su biografía: ")
                                estudiante3_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante3_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")
                                esperar_input()
                case "b":
                    print("En construcción.")
                    esperar_input()
                    submenu = ""
                case "c":
                    submenu = ""
                    menu = ""
                case _:
                    print("Opción invalida. Intente de nuevo.")
                    esperar_input()
                    submenu = ""
            
        case "2":
            if submenu == "":
                print("\nGestionar candidatos.")
                print("\na. Ver Candidatos")
                print("b. Reportar a un candidato.")
                print("c. Volver\n")
                submenu = input("Ingrese una opción: ")
                clear()
            match submenu:
                case "a":
                    clear()
                    if submenu_2 == "":
                        print("Informacion de los candidatos:")
                        mostrar_datos_estudiante(estudiante1_nombre, estudiante1_nacimiento, estudiante1_biografia, estudiante1_hobbies)
                        mostrar_datos_estudiante(estudiante2_nombre, estudiante2_nacimiento, estudiante2_biografia, estudiante2_hobbies)
                        mostrar_datos_estudiante(estudiante3_nombre, estudiante3_nacimiento, estudiante3_biografia, estudiante3_hobbies)
                        print("\n\nOpciones:")
                        print("\na. Dar me gusta")
                        print("b. Volver\n")
                        submenu_2 = input("Ingrese una opción: ")
                        clear()
                    match submenu_2:
                        case "a":
                            nombre_me_gusta = input("Ingrese el nombre del usuario al que desea darle me gusta: ")
                            nombre_es_valido = nombre_me_gusta == estudiante1_nombre or nombre_me_gusta == estudiante2_nombre or nombre_me_gusta == estudiante3_nombre
                            if nombre_es_valido:
                                if usuario_log == estudiante1_email:
                                    estudiante1_me_gusta = nombre_me_gusta
                                if usuario_log == estudiante2_email:
                                    estudiante2_me_gusta = nombre_me_gusta
                                if usuario_log == estudiante3_email:
                                    estudiante3_me_gusta = nombre_me_gusta
                                clear()
                                print(f"Le diste me gusta al usuario: {nombre_me_gusta}")
                            else:
                                clear()
                                print(f"El nombre {nombre_me_gusta} no pertenece a ningun usuario.")
                            submenu_2 = ""
                            esperar_input()
                        case "b":
                            submenu_2 = ""
                            submenu = ""
                        case _:
                            print ("Opción invalida. Intente de nuevo.")
                            submenu_2 = ""
                            esperar_input()

                case "b":
                    print("En construcción.")
                    submenu = ""
                    esperar_input()
                case "c":
                    menu = ""
                    submenu = ""
                case _: 
                    print ("Opción invalida. Intente de nuevo.")
                    submenu = ""
                    esperar_input()

        case "3":
            print("\nMatcheos.")
            print("\na. Ver Matcheos.")
            print("b. Eliminar Matcheos.")
            print("c. Volver\n")
            submenu = input("Ingrese una opción: ")
            clear()
            match submenu:
                case "a":
                    print ("En construcción")
                    esperar_input()
                case "b":
                    print("En construcción.")
                    esperar_input()
                case "c":
                    menu = ""
                    submenu = ""
                case _: 
                    print ("Opción invalida. Intente de nuevo")
                    esperar_input()
        
        case "4":
            print("\nEn Construcción")
            esperar_input()
            menu = ""
        
        case "0":
            print("Saliendo...")

        case _:
            print("Opción invalida. Intente de nuevo.")
            esperar_input()
            menu = ""


