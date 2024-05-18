#from pwinput import pwinput#
from getpass import getpass
from datetime import datetime

debug = True

estudiante1_email = "estudiante1@ayed.com"
estudiante1_contraseña = "111222"
estudiante1_hobbies = ""   
estudiante1_nacimiento = ""
estudiante1_biografia = ""


estudiante2_email = "estudiante2@ayed.com"
estudiante2_contraseña = "333444"
estudiante2_hobbies = ""   
estudiante2_nacimiento = ""
estudiante2_biografia = ""

estudiante3_email = "estudiante3@ayed.com" 
estudiante3_contraseña = "555666"
estudiante3_hobbies = ""   
estudiante3_nacimiento = ""
estudiante3_biografia = ""

intento = 0
usuario_log = ""
email_correcto = False

if debug:
    usuario_log = estudiante1_email
    
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
    print("\nBienvenido, ¿Que desea hacer?")
   
else:
    print("Acceso invalido.")

## menu interactivo ##
menu = ""
submenu = ""

while menu != "0":
    if menu == "":    
        print("\n1. Gestionar mi perfil")
        print("2. Gestionar candidatos")  
        print("3. Matcheos")
        print("4. Reportes estadísticos")
        print("0. Salir\n")
        menu = input("Ingrese una opción: ")
    match menu:
        case "1":
            ## opción 1. gestionar mi perfil ##
            
            if submenu == "":
                print("\nGestión de Perfil.")
                print("\na. Editar mis datos personales")
                print("b. Eliminar mi perfil")
                print("c. Volver\n")
                submenu = input("Ingrese una opción: ")
            match submenu.lower():
                case "a":
                    if usuario_log == estudiante1_email:
                        print("\na. Editar datos personales\n")
                        print(f"1. Fecha de Nacimiento (actúal: {estudiante1_nacimiento}): ")
                        print(f"2. Biografia (actúal: {estudiante1_biografia}): ")
                        print(f"3. Hobbies (actúal: {estudiante1_hobbies}): ")
                        print(f"0. Volver")

                        modificacion=input("Ingrese una opción: ")
                        match modificacion:
                            case "1":
                                dato = input("ingrese su fecha de nacimento (DD/MM/AAAA): ")
                                estudiante1_nacimiento = dato
                            case "2":
                                dato = input("ingrese su biografía: ")
                                estudiante1_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante1_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")

                    if usuario_log == estudiante2_email:
                        print("\na. Editar datos personales\n")
                        print(f"1. Fecha de Nacimiento (actúal: {estudiante2_nacimiento}) : ")
                        print(f"2. Biografia (actúal: {estudiante2_biografia}): ")
                        print(f"3. Hobbies (actúal: {estudiante2_hobbies}): ")
                        print(f"0. Volver")

                        modificacion=input("Ingrese una opción: ")
                        match modificacion:
                            case "1":
                                dato = input("ingrese su fecha de nacimento (DD/MM/AAAA): ")
                                estudiante2_nacimiento = dato
                            case "2":
                                dato = input("ingrese su biografía: ")
                                estudiante2_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante2_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")

                    if usuario_log == estudiante3_email:
                        print("\na. Editar datos personales\n")
                        print(f"1. Fecha de Nacimiento (actúal: {estudiante3_nacimiento}): ")
                        print(f"2. Biografia (actúal: {estudiante3_biografia}): ")
                        print(f"3. Hobbies (actúal: {estudiante3_hobbies}): ")
                        print(f"0. Volver")

                        modificacion=input("Ingrese una opción: ")
                        match modificacion:
                            case "1":
                                dato = input("ingrese su fecha de nacimento (DD/MM/AAAA): ")
                                estudiante3_nacimiento = dato
                            case "2":
                                dato = input("ingrese su biografía: ")
                                estudiante3_biografia  = dato
                            case "3":
                                dato = input("Ingrese sus hobbies: ")
                                estudiante3_hobbies = dato
                            case "0":
                                submenu = ""
                            case _:
                                print("Opción invalida. Intente de nuevo.")
                case "b":
                    # TODO
                    print("En construcción.")
                    submenu = ""
                case "c":
                    submenu = ""
                    menu = ""
                case _:
                    print("Opción invalida. Intente de nuevo.")
                    submenu = ""
            
        case "2":
            print("\nGestionar candidatos.")
            print("\na. Ver Candidatos")
            print("b. Reportar a un candidato.")
            print("c. Volver")
            submenu = input("Ingrese una opción: ")
            match submenu:
                case "a":
                    print ("En construcción")
                case "b":
                    print("En construcción.")
                case "c":
                    menu = ""
                    submenu = ""
                case _: 
                    print ("En construcción")

        case "3":
            print("\nMatcheos.")
            print("\na. Ver Matcheos.")
            print("b. Eliminar Matcheos.")
            print("c. Volver")
            submenu = input("Ingrese una opción: ")
            match submenu:
                case "a":
                    print ("En construcción")
                case "b":
                    print("En construcción.")
                case "c":
                    menu = ""
                    submenu = ""
                case _: 
                    print ("En construcción")
        
        case "4":
            print("\nEn Construcción")
            menu = ""
        
        case "0":
            print("Saliendo...")
        case _:
            print("Opción invalida. Intente de nuevo.")
            menu = ""


