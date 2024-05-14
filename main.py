estudiante1_email = "estudiante1@ayed.com"
estudiante1_contraseña = "111222"   


estudiante2_email = "estudiante2@ayed.com"
estudiante2_contraseña = "333444"

estudiante3_email = "estudiante3@ayed.com" 
estudiante3_contraseña = "555666"

intento = 0

ingreso = False

email_correcto = False

## sistema log-in, hasta 3 intentos ##

while intento < 3 and not ingreso:
    if not email_correcto:
        texto = input("ingrese su correo: ")
    if texto == estudiante1_email:
        email_correcto = True
        contraseña = input("ingrese su contraseña: ")
        if contraseña == estudiante1_contraseña:
            ingreso = True 
        else: 
            print("contraseña incorrecta,intente de nuevo.")
            intento = intento+1

    elif texto == estudiante2_email:
        email_correcto = True
        contraseña = input("ingrese su contraseña: ")
        if contraseña == estudiante2_contraseña:
            ingreso = True 
        else: 
            print("contraseña incorrecta,intente de nuevo.")
            intento = intento+1

    elif texto == estudiante3_email:
        email_correcto = True
        contraseña = input("ingrese su contraseña: ")
        if contraseña == estudiante3_contraseña:
            ingreso = True 
        else: 
            print("contraseña incorrecta,intente de nuevo.")
            intento=intento+1

    else: 
        print("Mail inválido. Intente de nuevo.")
        intento= intento+1

if ingreso:
    print("Acceso correcto!")
else:
    print("Acceso invalido.")

## menu interactivo ##

if ingreso == True:
    print("Bienvenido!,que quieres hacer?")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos(En Construcción)")  
    print("3. Matcheos(En Construcción)")
    print("4. Reportes estadísticos(En Construcción)")

    ## opción 1. gestionar mi perfil  ##
    orden =int(input("Indique con el número correspondiente: "))
    if orden == "1":
        print("Gestión de Perfil.")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil (En Construcción)")
        print("c. Volver")
        
        if orden == "2":
            ()