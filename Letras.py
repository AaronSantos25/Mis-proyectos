import random

def obtener_palabra_aleatoria():
    palabras = ["manzana", "perro", "gato", "python", "programacion"]
    return random.choice(palabras)

def jugar_adivinanzas():
    palabra = obtener_palabra_aleatoria()
    intentos = 0
    max_intentos = 5
    adivinada = False
    letras_adivinadas = []

    print("¡Bienvenido al juego de adivinanzas!")
    print("Adivina la palabra ingresando una letra a la vez. Tienes un máximo de", max_intentos, "intentos.")

    while intentos < max_intentos and not adivinada:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto! La letra está en la palabra.")
        else:
            print("Incorrecto. La letra no está en la palabra.")
            intentos += 1

        palabra_actual = ""
        for letra_palabra in palabra:
            if letra_palabra in letras_adivinadas:
                palabra_actual += letra_palabra
            else:
                palabra_actual += "_"

        print("Palabra actual:", palabra_actual)

        if palabra_actual == palabra:
            adivinada = True
            print("¡Felicidades! ¡Has adivinado la palabra!")
        elif intentos == max_intentos:
            print("Lo siento, has agotado tus intentos. La palabra correcta era:", palabra)

jugar_adivinanzas()
