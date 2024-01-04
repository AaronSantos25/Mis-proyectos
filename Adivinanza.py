import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0

    print("¡Bienvenido a 'Adivina el número'!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Intenta adivinar el número: "))
        intentos_realizados += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
            break

adivina_el_numero()
