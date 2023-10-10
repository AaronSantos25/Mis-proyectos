import pandas as pd
datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], 'Ventas':[30500, 35600, 28300, 33900, 30200, 29500, 31020, 12500, 29030, 25300, 35300, 40200], 'Gastos':[22000, 23400, 18100, 20700, 20700, 30600, 14200, 25300, 10020, 14200, 23500, 12900]}
contabilidad = pd.DataFrame(datos)
print(contabilidad)
