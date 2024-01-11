import random
import string
import tkinter as tk
from tkinter import messagebox

def generar_usuario():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    usuario = nombre.lower() + "." + apellido.lower()
    usuario_label.config(text="Usuario: " + usuario)

def generar_contrasena():
    longitud = int(longitud_entry.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    contrasena_label.config(text="Contraseña: " + contrasena)

def generar_usuario_y_contrasena():
    generar_usuario()
    generar_contrasena()

def mostrar_mensaje():
    messagebox.showinfo("¡Éxito!", "Usuario y contraseña generados correctamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de usuarios y contraseñas")

# Crear los elementos de la interfaz
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_label.pack()
apellido_entry = tk.Entry(ventana)
apellido_entry.pack()

longitud_label = tk.Label(ventana, text="Longitud de la contraseña:")
longitud_label.pack()
longitud_entry = tk.Entry(ventana)
longitud_entry.pack()

generar_btn = tk.Button(ventana, text="Generar", command=generar_usuario_y_contrasena)
generar_btn.pack()

usuario_label = tk.Label(ventana, text="")
usuario_label.pack()

contrasena_label = tk.Label(ventana, text="")
contrasena_label.pack()

mensaje_btn = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
mensaje_btn.pack()

# Iniciar el bucle de la aplicación
ventana.mainloop()
