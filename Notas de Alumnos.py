def validar_notas(notas):
    aprobados = []
    reprobados = []
    
    for nombre, nota in notas.items():
        if nota >= 50:
            aprobados.append(nombre)
        else:
            reprobados.append(nombre)
    
    return aprobados, reprobados

# Alumnos
notas_alumnos = {
    "Juan": 80,
    "María": 55,
    "Pedro": 70,
    "Ana": 45,
    "Luis": 90,
    "Andres":75,
    "Cesar":30,
    "Francisco":20,
    
}

aprobados, reprobados = validar_notas(notas_alumnos)

print("Aprobados:")
for alumno in aprobados:
    print(alumno)

print("\nReprobados:")
for alumno in reprobados:
    print(alumno)
