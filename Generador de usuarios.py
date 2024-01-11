import random
import string

def generar_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    apellido = input("Ingresa el apellido del usuario: ")
    usuario = nombre.lower() + "." + apellido.lower()
    return usuario

def generar_contrasena():
    longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_usuario_y_contrasena():
    usuario = generar_usuario()
    contrasena = generar_contrasena()
    return usuario, contrasena

def mostrar_menu():
    print("1. Generar usuario y contraseña")
    print("2. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario, contrasena = generar_usuario_y_contrasena()
            print("Usuario:", usuario)
            print("Contraseña:", contrasena)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

ejecutar_programa()
