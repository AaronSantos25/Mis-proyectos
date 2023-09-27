print("Hola esta es la calculadora.")
print("Dime que numeros usaras")
n1 = int(input("Que numero usara primero:"))
n2 = int(input("Que numero usara segundo:"))
n3 = int(input("Que numero usara de tercero:"))
print("""
1 . Suma y resta de elementos
2 . Multiplicar y dividir elementos
3 . Suma y multiplicar elementos
4 . Resta y multiplicar elementos
5 . Suma y Dividir elementos
6 . Apagar calculadora.
""")
opcion = int(input("Opcion por favor: "))
if opcion == 1:
    print(" ")
    print("RESULTADO de",n1,"+",n2, "-",n3, "es", n1+n2-n3)
elif opcion == 2:
    print(" ")
    print("RESULTADO de",n1,"*",n2, "/",n3, "es", n1*n2/n3)
elif opcion == 3:
    print (" ")
    print("RESULTADO de",n1,"+",n2, "*",n3, "es", n1+n2*n3)
elif opcion == 4:
    print(" ")
    print("RESULTADO de",n1,"-",n2, "*",n3, "es", n1-n2*n3)
elif opcion == 5:
    print (" ")
    print("RESULTADO de",n1,"+",n2, "/",n3, "es", n1+n2/n3)
elif opcion == 6:
    print(" ")

    print("Opcion incorrecta")
    
