print("Bienvenido al sistema de contraseñas Laica. ")
print("Vamos a generar una contraseña para el sistema. ")
usuario = input("Coloque el nombre del usuario: ")
print("Muy bien usuario " + usuario , "su contraseña esta siendo procesada. ")
import random
minusculas = 'abcdefghijklmñnopqrstuvwxyz'
mayusculas = 'ABCDEFGHIJKLMÑNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '[]{}%&$;._/\()-?¿¡!ª><=:ç^+*'
caracteres = minusculas + mayusculas + numeros + simbolos
passlongitud = 16
password = " ".join(random.sample(caracteres, passlongitud))
print(password)
print("El usuario " + usuario , "ya posee una contraseña generada por el sistema. ")
