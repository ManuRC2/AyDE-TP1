from pwinput import pwinput
from getpass import getpass

debug = True

estudiante1_email = "estudiante1@ayed.com"
estudiante1_contraseña = "111222"   

estudiante2_email = "estudiante2@ayed.com"
estudiante2_contraseña = "333444"

estudiante3_email = "estudiante3@ayed.com" 
estudiante3_contraseña = "555666"

intento = 0
ingreso = False
email_correcto = False
menu = False

if debug:
    ingreso = True

## sistema log-in, hasta 3 intentos ##

while intento < 3 and not ingreso:
    if not email_correcto:
        texto = input("Ingrese su correo: ")
    if texto == estudiante1_email:
        email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante1_contraseña:
            ingreso = True 
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento = intento+1

    elif texto == estudiante2_email:
        email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante2_contraseña:
            ingreso = True 
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento = intento+1

    elif texto == estudiante3_email:
        email_correcto = True
        contraseña = getpass(f"Ingrese la contraseña para {texto}: ")
        if contraseña == estudiante3_contraseña:
            ingreso = True 
        else: 
            print("Contraseña incorrecta, intente de nuevo.")
            intento=intento+1

    else: 
        print("Correo inválido. Intente de nuevo.")
        intento = intento + 1

if ingreso:
    print("Acceso correcto!")
    print("\nBienvenido, ¿Que desea hacer?")
    menu = True
else:
    print("Acceso invalido.")

## menu interactivo ##

while menu:
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")  
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir\n")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            ## opción 1. gestionar mi perfil ##
            submenu = True
            while submenu:
                print("\nGestión de Perfil.")
                print("\na. Editar mis datos personales")
                print("b. Eliminar mi perfil")
                print("c. Volver\n")
                opcion = input("Ingrese una opción: ")
                match opcion.lower():
                    case "a":
                        # TODO
                        print("En construcción.")
                    case "b":
                        # TODO
                        print("En construcción.")
                    case "c":
                        submenu = False
                    case _:
                        print("Opción invalida. Intente de nuevo.")
        case "2":
            # TODO
            print("En construcción.")
        case "3":
            print("En construcción.")
        case "4":
            print("En construcción.")
        case "0":
            print("Saliendo...")
            menu = False
        case _:
            print("Opción invalida. Intente de nuevo.")