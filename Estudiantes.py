rint("Bienvenido a este sistema de promedios academicos.")
print("Para calcular sus notas vamos a necesitar sus datos")
nombre= input("Por favor coloque su nombre y apellido: ")
print("Muy bien estudiante: " + nombre,  "vamos a calcular sus notas.")
n1= int(input("Ingrese su nota de ingles: "))
n2= int(input("Ingrese su nota de historia: "))
n3= int(input("Ingrese su nota de quimica: "))
n4= int(input("Ingrese su nota de matematica: "))
n5= int(input("Ingrese su nota de fisica: "))
n6= (n1+n2+n3+n4+n5)/5
if n6 >=10:
    print("Estudiante " + nombre , "aprobo de año con un promedio de: ")
    print(n6)
else:
    print("Estudiante " + nombre , "reprobo de año con un promedio de: ")
    print(n6)
