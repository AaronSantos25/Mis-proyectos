usuarios = {}  # Diccionario para almacenar los usuarios y claves

def registrar_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    while nombre in usuarios:
        print("El nombre de usuario ya está en uso. Intente nuevamente.")
        nombre = input("Ingrese su nombre de usuario: ")
    
    clave = input("Ingrese su contraseña: ")
    usuarios[nombre] = clave
    print("Registro exitoso.\n")

def iniciar_sesion():
    nombre = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")
    
    if nombre in usuarios and usuarios[nombre] == clave:
        print("Inicio de sesión exitoso.\n")
    else:
        print("Nombre de usuario o contraseña incorrectos.\n")

while True:
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.\n")
