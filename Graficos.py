import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_evolucion_ventas(ventas, tipo):
    '''Función que construye un diagrama del tipo indicado con la evolución de las ventas por años.
    
    Parámetros:
        - ventas: Es un dataframe de Pandas con las ventas, siendo el índice los años.
        - tipo: Es una cadena con el tipo de gráfico a dibujar: lineas, barras, sectores o areas.

    Salida:
        Un gráfico del tipo indicado con la evolución de las ventas.
    '''
    
    graficos = {'lineas':'line', 'barras':'bar', 'sectores':'pie', 'area':'area'}
   
    fig, ax = plt.subplots()
    
    ventas.plot(kind = graficos[tipo], ax = ax)
    
    plt.title('Evolución del número de ventas')
    
    return ax

df_ventas = pd.Series([10538, 4544, 3865, 1200, 500], index = [2000, 2001, 2002, 2003, 2004])
diagrama_evolucion_ventas(df_ventas, 'lineas')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'area')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'barras')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'sectores')
plt.show()
