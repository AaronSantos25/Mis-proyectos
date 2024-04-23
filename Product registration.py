import os
from PIL import Image

def buscar_imagenes(carpeta):
    imagenes = []
    extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
    
    for archivo in os.listdir(carpeta):
        if any(archivo.lower().endswith(ext) for ext in extensiones_validas):
            imagenes.append(os.path.join(carpeta, archivo))
    
    return imagenes

def mostrar_imagenes(imagenes):
    for imagen in imagenes:
        img = Image.open(imagen)
        img.show()

# Carpeta donde se encuentran las imágenes
carpeta_imagenes = "ruta/a/la/carpeta"

# Buscar imágenes en la carpeta
imagenes_encontradas = buscar_imagenes(carpeta_imagenes)

# Mostrar las imágenes encontradas
mostrar_imagenes(imagenes_encontradas)
