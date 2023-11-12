def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

print("Calculadora básica")
print("------------------")

while True:
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = restar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
    
    print()  # Línea en blanco para mejorar la legibilidad
