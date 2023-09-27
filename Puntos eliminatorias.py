import matplotlib.pyplot as plt 

def diagrama_barras_venezuela(venezuela, color):
    '''Función que construye un diagrama de barras con las notas de las asignaturas de un curso.
    
    Parámetros:
        - puntos: Es un diccionario formado por pares con clave el nombre de la seleccion y los puntos logrados
        - color: Es una cadena con el color de las barras.
    
    Salida:
        - Un diagrama de barras con los puntos del diccionario.
    '''
    
    fig, ax = plt.subplots()
   
    ax.bar(puntos.keys(), puntos.values(), color = color)
    
    return ax

puntos = {'2006':18, '2010':22, '2014':22, '2018': 12, '2022':10}
diagrama_barras_venezuela(puntos, 'blue')
plt.show()
