#from pwinput import pwinput#
from getpass import getpass
from datetime import datetime
import os

################ FUNCIONES ################

# funcion para limpiar consola
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# esperar input del usuario para continuar
def esperar_input():
    # uso getpass para que no se vean los caracteres que se ingresan
    getpass("\nPresione enter para continuar...")

# calcula la edad de una persona dada su fecha de nacimiento en formato (AAAA-MM-DD)
def calcular_edad(fecha_nacimiento):
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

# imprime el menú si es necesario, y devuelve el valor del menu al que se tiene que entrar
def ingresar_menu(menu):
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

# funcion que parsea correctamente la entrada de las fechas de nacimiento
# se guarda el string de entradda, y no la fecha parseada en formato Datetime, porque asi es indicado en el enunciado
def ingresar_fecha_nacimiento():
    fecha_parseada = ""
    while not fecha_parseada:
        entrada = input("Ingrese su fecha de nacimento (AAAA-MM-DD): ")
        try:
            fecha_parseada = datetime.strptime(entrada, "%Y-%m-%d")
        except Exception as e:
            clear()
            print("Por favor, verifique que el formato de la fecha ingresada sea correcto.\n")
    return entrada

# funcion que imprime el menú para editar datos personales, con los datos especificados del estudiante
def menu_editar_datos_personales(nacimiento, biografia, hobbies):
    print("\na. Editar datos personales\n")
    print(f"1. Fecha de Nacimiento (actual: {nacimiento}): ")
    print(f"2. Biografia (actual: {biografia}): ")
    print(f"3. Hobbies (actual: {hobbies}): ")
    print(f"0. Volver\n")

    modificacion = input("Ingrese una opción: ")
    clear()
    return modificacion

# muestra los datos brindados de un estudiante
def mostrar_datos_estudiante(nombre, fecha_nacimiento, biografia, hobbies):
    print(f"\nNombre: {nombre}")
    print(f"Fecha de nacimiento: {fecha_nacimiento}")
    print(f"Edad: {calcular_edad(fecha_nacimiento)}")
    print(f"Biografía: {biografia}")
    print(f"Hobbies: {hobbies}")

################ VARIABLES ################

debug = True

estudiante1_email = "estudiante1@ayed.com"
estudiante1_contraseña = "111222"
estudiante1_nombre = "Estudiante1"
estudiante1_hobbies = ""
estudiante1_nacimiento = ""
estudiante1_biografia = ""
estudiante1_me_gusta = ""

estudiante2_email = "estudiante2@ayed.com"
estudiante2_contraseña = "333444"
estudiante2_nombre = "Estudiante2"
estudiante2_hobbies = ""
estudiante2_nacimiento = ""
estudiante2_biografia = ""
estudiante2_me_gusta = ""

estudiante3_email = "estudiante3@ayed.com" 
estudiante3_contraseña = "555666"
estudiante3_nombre = "Estudiante3"
estudiante3_hobbies = ""
estudiante3_nacimiento = ""
estudiante3_biografia = ""
estudiante3_me_gusta = ""

intento = 0
usuario_log = ""
email_correcto = False

if debug:
    usuario_log = estudiante1_email
    estudiante1_nacimiento = "2003-02-22"
    estudiante2_nacimiento = "2006-12-22"
    estudiante3_nacimiento = "2005-12-22"
    
## sistema log-in, hasta 3 intentos ##

while intento < 3 and not usuario_log:
    
    if not email_correcto:
        texto = input("Ingrese su correo: ")
        if texto == estudiante1_email:
            email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante1_contraseña:
            usuario_log = estudiante1_email
        
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento = intento+1

    elif texto == estudiante2_email:
        email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante2_contraseña:
            usuario_log = estudiante2_email 
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento = intento+1

    elif texto == estudiante3_email:
        email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante3_contraseña:
            usuario_log = estudiante3_email
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento=intento+1

    else: 
        print("Correo inválido. Intente de nuevo.")
        intento = intento + 1

if usuario_log:
    print("Acceso correcto!")
   
else:
    print("Acceso invalido.")

## menu interactivo ##
menu = ""
submenu = ""
submenu_2 = ""

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


