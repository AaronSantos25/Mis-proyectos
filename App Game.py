import random
import tkinter as tk
from tkinter import messagebox

palabras = ["manzana", "banana", "naranja", "limón", "pera"]

def iniciar_juego():
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos_restantes = 6

    def verificar_letra():
        nonlocal intentos_restantes
        letra_ingresada = letra_entry.get().lower()

        if letra_ingresada in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra_ingresada:
                    letras_adivinadas[i] = letra_ingresada
            palabra_label.config(text=" ".join(letras_adivinadas))
            if "_" not in letras_adivinadas:
                messagebox.showinfo("¡Felicidades!", "¡Has adivinado la palabra!")
                reiniciar_juego()
        else:
            intentos_restantes -= 1
            intentos_label.config(text="Intentos restantes: {}".format(intentos_restantes))
            if intentos_restantes == 0:
                messagebox.showinfo("¡Fin del juego!", "¡Has perdido! La palabra secreta era '{}'.".format(palabra_secreta))
                reiniciar_juego()

        letra_entry.delete(0, tk.END)

    def reiniciar_juego():
        nonlocal intentos_restantes
        intentos_restantes = 6
        palabra_secreta = random.choice(palabras).lower()
        letras_adivinadas = ["_"] * len(palabra_secreta)
        palabra_label.config(text=" ".join(letras_adivinadas))
        intentos_label.config(text="Intentos restantes: {}".format(intentos_restantes))

    # Crear la ventana principal
    ventana_juego = tk.Toplevel(ventana)
    ventana_juego.title("Adivina la palabra")

    # Crear los elementos de la interfaz
    instrucciones_label = tk.Label(ventana_juego, text="Ingresa una letra:")
    instrucciones_label.pack()

    letra_entry = tk.Entry(ventana_juego)
    letra_entry.pack()

    verificar_btn = tk.Button(ventana_juego, text="Verificar", command=verificar_letra)
    verificar_btn.pack()

    palabra_label = tk.Label(ventana_juego, text=" ".join(letras_adivinadas))
    palabra_label.pack()

    intentos_label = tk.Label(ventana_juego, text="Intentos restantes: {}".format(intentos_restantes))
    intentos_label.pack()

    reiniciar_btn = tk.Button(ventana_juego, text="Reiniciar", command=reiniciar_juego)
    reiniciar_btn.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de adivinar palabras")

# Crear los elementos de la interfaz
titulo_label = tk.Label(ventana, text="¡Bienvenido al juego de adivinar palabras!")
titulo_label.pack()

inicio_btn = tk.Button(ventana, text="Iniciar juego", command=iniciar_juego)
inicio_btn.pack()

# Iniciar el bucle de la aplicación
ventana.mainloop()
