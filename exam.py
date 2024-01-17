class Pregunta:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

class Evaluacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
    
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    def tomar_examen(self):
        calificacion = 0
        total_preguntas = len(self.preguntas)
        
        for pregunta in self.preguntas:
            print(pregunta.enunciado)
            respuesta = input("Ingrese su respuesta: ")
            
            if respuesta == pregunta.respuesta_correcta:
                calificacion += 1
        
        porcentaje_calificacion = (calificacion / total_preguntas) * 100
        print(f"Su calificación final es: {porcentaje_calificacion}%")

# Crear una evaluación
evaluacion = Evaluacion("Examen de Matemáticas")

# Agregar preguntas a la evaluación
pregunta1 = Pregunta("¿Cuánto es 20 + 30?", "50")
pregunta2 = Pregunta("¿Cuál es la raíz cuadrada de 81?", "9")
pregunta3 = Pregunta("¿Cuál es el resultado de 5 * 7?", "35")
pregunta4 = Pregunta("¿Cuánto es 40 / 2?", "20")
pregunta5 = Pregunta("¿Cuánto es el resultado de 2 + 9 - 5?", "6")
pregunta6 = Pregunta("¿Cuánto es el resultado de 3 * 20 / 4?", "15")
pregunta7 = Pregunta("¿Cuánto es el resultado de 1 + 5 - 2 * 4 / 8?" , "2")

evaluacion.agregar_pregunta(pregunta1)
evaluacion.agregar_pregunta(pregunta2)
evaluacion.agregar_pregunta(pregunta3)
evaluacion.agregar_pregunta(pregunta4)
evaluacion.agregar_pregunta(pregunta5)
evaluacion.agregar_pregunta(pregunta6)
evaluacion.agregar_pregunta(pregunta7)

# Tomar el examen
evaluacion.tomar_examen()
