import random

def juego_matematicas():
    operaciones = ['+', '-', '*', '/']
    operacion = random.choice(operaciones)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    else:
        resultado = num1 / num2

    print("¡Bienvenido a 'Juego de Matemáticas'!")
    print(f"¿Cuál es el resultado de {num1} {operacion} {num2}?")

    while True:
        respuesta = float(input("Ingresa tu respuesta: "))

        if respuesta == resultado:
            print("¡Correcto! ¡Has ganado!")
            break
        else:
            print("Incorrecto. Inténtalo nuevamente.")

juego_matematicas()
