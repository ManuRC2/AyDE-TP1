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

# menu para moderadores

def ingresar_menu_mods(menu: str):
    clear()

    if menu != "":
        return menu

    print("\nBienvenido, ¿Que desea hacer?")
    print("\n1. Gestionar usuarios")
    print("2. Gestionar Reportes")
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
REPORTES_MAX = 10

# [id, estado, email, contraseña, nombre, hobbies, nacimiento, biografia]
estudiantes = [[""]*8 for n in range(ESTUDIANTES_MAX)]
for id in range(ESTUDIANTES_MAX):
    estudiantes[id][0] = str(id)
    estudiantes[id][1] = "INACTIVO"
estudiantes[0] = ["0", "ACTIVO", "estudiante1@ayed.com", "111111", "Estudiante1", "a", "", "f"]
estudiantes[1] = ["1", "ACTIVO", "estudiante2@ayed.com", "222222", "Estudiante2", "b", "", "g"]
estudiantes[2] = ["2", "ACTIVO", "estudiante3@ayed.com", "333333", "Estudiante3", "c", "", "h"]
estudiantes[3] = ["3", "ACTIVO", "estudiante4@ayed.com", "444444", "Estudiante4", "d", "", "i"]

moderadores = [[""]*8 for n in range(MODERADORES_MAX)]
for id in range(MODERADORES_MAX):
    moderadores[id][0] = str(id)
    moderadores[id][1] = "INACTIVO"
moderadores[0] = ["0", "ACTIVO", "moderador1@ayed.com", "mod111", "Moderador1", "", "", ""]

likes = [[False]*ESTUDIANTES_MAX for n in range(ESTUDIANTES_MAX)]

# [id, estado, id_reportante, id_reportado, razon]
reportes = [[""]*5 for n in range(REPORTES_MAX)]
for id in range(REPORTES_MAX):
    reportes[id][0] = str(id)

usuario_log: str = ""
menu: str = ""
submenu: str = ""
submenu_2: str = ""
submenu_3: str = ""

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
        print("Bienvenido! Identifiquese para ingresar al programa.\n")
        print("1. Loguearse")
        print("2. Registrarse")
        print("0. Salir\n")

        opcion = input("Ingrese una opción: ")
        
        clear()

        match opcion:
            case "1":
                if cantidad_moderadores() < MODERADORES_MIN:
                    print(f"No hay suficientes moderadores registrados. Por favor, contacte a un administrador.")
                elif cantidad_estudiantes() < ESTUDIANTES_MIN:
                    print(f"No hay suficientes estudiantes registrados. Por favor, registrese.")
                else:
                    return ingresar()
            case "2":
                registrar()
            case "0":
                return 0
            case _:
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


def get_usuario_por_id(id: str):
    for estudiante in estudiantes:
        if estudiante[0] == id:
            return estudiante
    return None


def get_tipo_usuario(email: str):
    for estudiante in estudiantes:
        if estudiante[2] == email:
            return "ESTUDIANTE"
    for moderador in moderadores:
        if moderador[2] == email:
            return "MODERADOR"
    return ""


def get_reporte_libre():
    for reporte in reportes:
        if reporte[1] != "0":
            return reporte[0]
    return "-1"

salir = False
while not salir:
    usuario_log = logueo_o_registrarse()
    tipo_usuario = ""

    clear()
    if usuario_log == 0:
        print("Saliendo del programa...")
        menu = "0"
        salir = True
    elif usuario_log:
        print("Acceso correcto! Ingresando al programa...")
        tipo_usuario = get_tipo_usuario(usuario_log[2])
        esperar_input()
    else:
        print("Acceso invalido. Saliendo del programa...")
        menu = "0"
        salir = True
    

    ## menu interactivo ##
    while menu != "0":
        match tipo_usuario:
            case "ESTUDIANTE":   
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
                                clear()
                                print("¿Esta seguro de que desea eliminar su perfil?\n")
                                print("1. Si")
                                print("2. No\n")
                                opcion = input("Ingrese una opción: ")
                                clear()
                                match opcion:
                                    case "1":
                                        usuario_log[1] = "INACTIVO"
                                        print("Perfil eliminado con éxito. Saliendo...")
                                        esperar_input()
                                        menu = "0"
                                        submenu = ""
                                    case "2":
                                        print("No se eliminó el perfil.")
                                        esperar_input()
                                        submenu = ""
                                    case _:
                                        print("Opción invalida. Intente de nuevo.")
                                        esperar_input()

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
                                            likes[int(usuario_log[0])][int(estudiante_mg[0])] = True
                                            clear()
                                            print(f"Le diste me gusta al usuario {nombre_mg}")
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
                                id_reporte = int(get_reporte_libre())
                                if id_reporte != -1:
                                    nombre_reporte = input("Ingrese el nombre del usuario al que desea reportar: ")
                                    estudiante_reporte = []
                                    for estudiante in estudiantes:
                                        if estudiante[4] == nombre_reporte and nombre_reporte:
                                            estudiante_reporte = estudiante
                                    clear()
                                    if estudiante_reporte:
                                        razon_reporte = input("Ingrese la razon del reporte: ")
                                        reportes[id_reporte] = [str(id_reporte), "0", usuario_log[0], estudiante_reporte[0], razon_reporte]
                                        clear()
                                        print(f"Reportaste al usuario {nombre_reporte}.")
                                    else:
                                        print(f"El nombre {nombre_reporte} no pertenece a ningun usuario.")
                                else:
                                    print("Se ha alcanzado el numero máximo de reportes pendientes. Por favor, espere a que un moderador los revise y vuelva a intentarlo.")
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
                        print("\nReportes estadísticos\n")
                        likes_correspondidos = 0
                        likes_dados = 0
                        likes_recibidos = 0
                        for n in range(ESTUDIANTES_MAX):
                            if likes[int(usuario_log[0])][n] and likes[n][int(usuario_log[0])]:
                                likes_correspondidos += 1
                            else:
                                if likes[int(usuario_log[0])][n]:
                                    likes_dados += 1
                                if likes[n][int(usuario_log[0])]:
                                    likes_recibidos += 1
                        porcentaje_correspondidos = likes_correspondidos*100/(cantidad_estudiantes()-1)
                        print(f"Matcheados sobre el % posible: {porcentaje_correspondidos}%")
                        print(f"Likes dados y no recibidos: {likes_dados}")
                        print(f"Likes recibidos y no respondidos: {likes_recibidos}")
                        esperar_input()
                        menu = ""

                    case "0":
                        print("Saliendo...")

                    case _:
                        print("Opción invalida. Intente de nuevo.")
                        esperar_input()
                        menu = ""

            case "MODERADOR":
                menu = ingresar_menu_mods(menu)
                match menu:
                    case "1":
                        # opcion 1, gestionar usuarios
                        clear()
                        if submenu == "":
                            print("Gestionar Usuarios")
                            print("\na. Desactivar Usuario")
                            print("b. Volver\n")
                            submenu = input("Ingrese una opción: ")
                            clear()
                        match submenu.lower():
                            case "a":
                                clear()
                                if submenu_2 == "":
                                    print("Desactivar Usuario\n")
                                    print("a. Buscar por ID")
                                    print("b. Buscar por nombre")
                                    print("c. Volver\n")
                                    submenu_2 = input("Ingrese una opcion: ")
                                    clear()
                                match submenu_2.lower():
                                    case "a":
                                        id_buscado = input("Ingrese el ID del usuario al que desea desactivar: ")
                                        id_desactivar = []
                                        for estudiante in estudiantes:
                                            if estudiante[0] == id_buscado and id_buscado:
                                                id_desactivar = estudiante
                                        if id_desactivar:
                                            usuario_log[0] = id_buscado
                                            estudiante[1] == "INACTIVO"
                                            clear()
                                            print(f"Se desactivo el usuario {estudiante[4]}")
                                        else:
                                            clear()
                                            print(f"El id {id_buscado} no pertenece a ningun usuario.")
                                        submenu_2 = ""
                                        esperar_input()

                                    case "b":
                                        print("En construcción.")
                                        submenu_2 = ""
                                        esperar_input()
                                    
                                    case "c":
                                        submenu_2 = ""
                                        submenu = ""

                            case "b":
                                submenu = ""
                                menu = ""

                            case _:
                                print("Opción invalida. Intente de nuevo.")
                                esperar_input()
                                submenu = ""

                    case "2":
                        # opcion 2, gestionar reportes
                        clear()
                        if submenu == "":
                            print("\nGestionar Reportes")
                            print("\na. Ver Reportes")
                            print("b. Volver\n")
                            submenu = input("Ingrese una opción: ")
                            clear()
                        match submenu.lower():
                            case "a":
                                for reporte in reportes:
                                    usuario_1 = get_usuario_por_id(reporte[2])
                                    usuario_2 = get_usuario_por_id(reporte[3])
                                    opcion_reporte = ""
                                    if reporte[1] == "0" and  usuario_1[1] == "ACTIVO" and usuario_2[1] == "ACTIVO":
                                        while not opcion_reporte:
                                            clear()
                                            print(f"Reporte {reporte[0]}")
                                            print(f"El usuario ({usuario_1[0]}) {usuario_1[4]} reporta al usuario ({usuario_2[0]}) {usuario_2[4]}")
                                            print(f"Razon: {reporte[4]}\n")
                                            print("¿Que desea hacer?\n")
                                            print("1. Ignorar reporte")
                                            print("2. Bloquear al usuario reportado\n")
                                            opcion_reporte = input("Eliga una opción: ")
                                            clear()

                                            match opcion_reporte:
                                                case "1":
                                                    reporte[1] = "2"
                                                    print("Reporte desestimado con éxito.")
                                                case "2":
                                                    reporte[1] = "1"
                                                    usuario_2[1] = "INACTIVO"
                                                    print(f"Usuario {usuario_2[4]} bloqueado. Reporte resuelto con éxito.")
                                                case _:
                                                    print("Opción invalida. Intente de nuevo.")
                                                    opcion_reporte = ""
                                        submenu = ""
                                        esperar_input()

                            case "b":
                                submenu = ""
                                menu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")
                                esperar_input()
                                submenu = ""

                    case "0":
                        print("Saliendo...")

                    case _:
                        print("Opción invalida. Intente de nuevo.")
                        esperar_input()
                        menu = ""
    menu = ""