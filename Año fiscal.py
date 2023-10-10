import pandas as pd
comienzo = int(input('Introduce el primer año fiscal: '))
final = int(input('Introduce el ultimo año fiscal: '))
ventas = {}
for i in range(comienzo, final+1):
    ventas[i] = float(input('Introduce las ventas por cada año ' + str(i) +': '))
ventas = pd.Series(ventas)
print('Ventas\n', ventas)
print('Ventas con descuento\n', ventas*0.9)
