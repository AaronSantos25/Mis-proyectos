def agregar_tarea(lista_tareas, tarea):
    lista_tareas.append(tarea)
    print("Tarea agregada:", tarea)

def completar_tarea(lista_tareas, indice):
    if indice < len(lista_tareas):
        tarea_completada = lista_tareas[indice]
        lista_tareas[indice] = f"[X] {tarea_completada}"
        print("Tarea completada:", tarea_completada)
    else:
        print("No existe la tarea con ese índice.")

def mostrar_tareas(lista_tareas):
    print("Lista de tareas:")
    for tarea in lista_tareas:
        print("-", tarea)

# Lista para almacenar las tareas
tareas = []

# Menú de la aplicación
while True:
    print("\n--- Aplicación de Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas, nueva_tarea)
    elif opcion == "2":
        indice_tarea = int(input("Ingrese el índice de la tarea a completar: "))
        completar_tarea(tareas, indice_tarea)
    elif opcion == "3":
        mostrar_tareas(tareas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
