################ INTEGRANTES ################
# Colusso Manuel
# Larrosa Joaquín
# Grandoso Emmanuel
# Aguirre Diego

################ DECLARADO DE VARIABLES ################

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

################ IMPORTACIONES ################

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

fecha_actual: date
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

    if not(mes_actual >= mes_nac and dia_actual >= dia_nac):
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

        email_correcto = False
        email = input("Ingrese su email: ")
        if email:
            for estudiante in estudiantes:
                if estudiante[1] == "ACTIVO":
                    if email == estudiante[2]:
                        email_correcto = True
                        contraseña = getpass(f"Ingrese la contraseña para {estudiante[4]}: ")
                        if contraseña == estudiante[3]:
                            logueado = estudiante
                        else: 
                            intentos = intentos - 1
                            print(f"Contraseña incorrecta. {intentos} intentos restantes.")
                            esperar_input()

            if not email_correcto:
                for moderador in moderadores:
                    if moderador[1] == "ACTIVO":
                        if email == moderador[2]:
                            email_correcto = True
                            contraseña = getpass(f"Ingrese la contraseña para {moderador[4]}: ")
                            if contraseña == moderador[3]:
                                logueado = moderador
                            else: 
                                intentos = intentos - 1
                                print(f"Contraseña incorrecta. {intentos} intentos restantes.")
                                esperar_input()

        if not email_correcto:
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
def menu_editar_datos_personales(usuario: list):
    print("\na. Editar datos personales\n")
    print(f"1. Fecha de Nacimiento (actual: {usuario[6]}): ")
    print(f"2. Biografia (actual: {usuario[7]}): ")
    print(f"3. Hobbies (actual: {usuario[5]}): ")
    print(f"0. Volver\n")

    opcion = input("Ingrese una opción: ")
    clear()
    return opcion

""" 
muestra los datos brindados de un estudiante
"""
def mostrar_datos_estudiante(estudiante: list):
    print(f"\nNombre: {estudiante[4]}")
    print(f"Fecha de nacimiento: {estudiante[6]}")
    print(f"Edad: {calcular_edad(estudiante[6])}")
    print(f"Biografía: {estudiante[7]}")
    print(f"Hobbies: {estudiante[5]}")

################ VARIABLES ################

ESTUDIANTES_MIN = 4
ESTUDIANTES_MAX = 8
MODERADORES_MIN = 1
MODERADORES_MAX = 4

# [id, estado, email, contraseña, nombre, hobbies, nacimiento, biografia, me_gusta]
estudiantes = [[""]*9 for n in range(ESTUDIANTES_MAX)]
for id in range(ESTUDIANTES_MAX):
    estudiantes[id][0] = str(id)
    estudiantes[id][1] = "INACTIVO"
estudiantes[0] = ["0", "ACTIVO", "estudiante1@ayed.com", "111111", "Estudiante1", "", "", "", ""]
estudiantes[1] = ["1", "ACTIVO", "estudiante2@ayed.com", "222222", "Estudiante2", "", "", "", ""]
estudiantes[2] = ["2", "ACTIVO", "estudiante3@ayed.com", "333333", "Estudiante3", "", "", "", ""]
estudiantes[3] = ["3", "ACTIVO", "estudiante4@ayed.com", "444444", "Estudiante4", "", "", "", ""]

moderadores = [[""]*9 for n in range(MODERADORES_MAX)]
for id in range(MODERADORES_MAX):
    moderadores[id][0] = str(id)
    moderadores[id][1] = "INACTIVO"
moderadores[0] = ["0", "ACTIVO", "moderador1@ayed.com", "mod111", "Moderador1", "", "", "", ""]

usuario_log: str = ""
menu: str = ""
submenu: str = ""
submenu_2: str = ""

################ PROGRAMA ################

def cantidad_estudiantes():
    usuarios = 0
    for estudiante in estudiantes:
        if estudiante[1] == "ACTIVO":
            usuarios += 1
    return usuarios


def cantidad_moderadores():
    usuarios = 0
    for moderador in moderadores:
        if moderador[1] == "ACTIVO":
            usuarios += 1
    return usuarios


def cantidad_usuarios():
    return cantidad_estudiantes() + cantidad_moderadores()


def primer_estudiante_libre():
    for estudiante in estudiantes:
        if estudiante[1] != "ACTIVO":
            return estudiante[0]
    else:
        return -1


def registrar():
    n_usuario = cantidad_estudiantes()
    
    if n_usuario >= ESTUDIANTES_MAX:
        print("Se alcanzó el máximo de usuarios. No se puede agregar otro.")
        esperar_input()
        return
    
    opcion = ""
    id_estudiante = int(primer_estudiante_libre())
    while opcion != "1" and opcion != "0":

        print("Ingrese los datos del nuevo estudiante")
        
        nombre = input("Nombre: ")

        email_valido = False
        while not email_valido:
            email_valido = True
            email = input("Email: ")
            for estudiante in estudiantes:
                if estudiante[2] == email:
                    email_valido = False
            if not email_valido:
                clear()
                print("El email ingresado ya está en uso por otro usuario.")
        
        contraseñas_iguales = False
        contraseña_valida = False
        while not (contraseñas_iguales and contraseña_valida):
            contraseña = getpass("Contraseña: ")

            if contraseña:
                contraseña_valida = True
                contraseña_confirm = getpass("Confirmar contraseña: ")
                
                if contraseña == contraseña_confirm:
                    contraseñas_iguales = True
                else:
                    clear()
                    print("Las contraseñas no coinciden. Por favor, vuelva a ingresarlas.")

            else:
                clear()
                print("Las contraseña no es válida. Por favor ingrese una diferente.")
        
        clear()
        print("Usted va a crear un usuario con los siguientes datos:\n")
        print("Email: ", email)
        print("Nombre: ", nombre)
        print("\n¿Desea continuar?\n")
        print("1. Continuar")
        print("2. Editar datos")
        print("0. Cancelar\n")
        opcion = input("Ingrese una opción: ")
        
        match opcion:
            case "1":
                clear()
                estudiantes[id_estudiante] = [str(id_estudiante), "ACTIVO", email, contraseña, nombre, '', '', '', '']
                print("Usuario creado con éxito.")
                esperar_input()
                clear()
            case "2":
                clear()
            case "0":
                clear()
                print("Creación del usuario cancelada.")
                esperar_input()

    return
                

def logueo_o_registrarse():

    opcion = ""

    while opcion != "0":
        
        clear()
        print("Bienvenido! Identifiquese para ingresar al programa.")
        print("1. Loguearse")
        print("2. Registrarse")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")
        
        match opcion:
            case "1":
                clear()
                if cantidad_moderadores() < MODERADORES_MIN:
                    print(f"No hay suficientes moderadores registrados. Por favor, contacte a un administrador.")
                elif cantidad_estudiantes() < ESTUDIANTES_MIN:
                    print(f"No hay suficientes estudiantes registrados. Por favor, registrese.")
                else:
                    return ingresar()
            case "2":
                clear()
                registrar()
            case "0":
                clear()
                return 0
            case _:
                clear()
                print("Opción invalida. Intente de nuevo.")
                esperar_input()


def get_usuario(email: str):
    for estudiante in estudiantes:
        if estudiante[2] == email:
            return estudiante
    for moderador in moderadores:
        if moderador[2] == email:
            return moderador
    return None


usuario_log = logueo_o_registrarse()

clear()
if usuario_log == 0:
    print("Saliendo del programa...")
    menu = "0"
elif usuario_log:
    print("Acceso correcto! Ingresando al programa...")
    esperar_input()
else:
    print("Acceso invalido. Saliendo del programa...")
    menu = "0"

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
                    modificacion = menu_editar_datos_personales(usuario_log)
                    match modificacion:
                        case "1":
                            usuario_log[6] = ingresar_fecha_nacimiento()
                        case "2":
                            dato = input("Ingrese su biografía: ")
                            usuario_log[7]  = dato
                        case "3":
                            dato = input("Ingrese sus hobbies: ")
                            usuario_log[5] = dato
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
                        for estudiante in estudiantes:
                            if estudiante[1] == "ACTIVO":
                                mostrar_datos_estudiante(estudiante)
                        print("\n\nOpciones:")
                        print("\na. Dar me gusta")
                        print("b. Volver\n")
                        submenu_2 = input("Ingrese una opción: ")
                        clear()
                    match submenu_2:
                        case "a":
                            nombre_mg = input("Ingrese el nombre del usuario al que desea darle me gusta: ")

                            estudiante_mg = []
                            for estudiante in estudiantes:
                                if estudiante[4] == nombre_mg and nombre_mg:
                                    estudiante_mg = estudiante
                            if estudiante_mg:
                                usuario_log[8] = nombre_mg
                                clear()
                                print(f"Le diste me gusta al usuario: {nombre_mg}")
                            else:
                                clear()
                                print(f"El nombre {nombre_mg} no pertenece a ningun usuario.")
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
