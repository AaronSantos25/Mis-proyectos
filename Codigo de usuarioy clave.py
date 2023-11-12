import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    longitud_contrasena = int(input("Ingrese la longitud de la contraseña: "))
    contrasena = generar_contrasena(longitud_contrasena)
    print("Usuario registrado correctamente.")
    print(f"Su contraseña generada es: {contrasena}")

# Ejecución del programa
registrar_usuario()
