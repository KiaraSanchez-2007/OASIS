from emociones import DetectorEmociones
from respiracion import Respiracion
from organizacion import Organizacion
from recursos import Recursos
from memoria import Memoria


class OasisChatbotV2:

    def __init__(self):

        # Módulos
        self.detector = DetectorEmociones()
        self.respiracion = Respiracion()
        self.organizacion = Organizacion()
        self.recursos = Recursos()
        self.memoria = Memoria()

        # Estado de conversación
        self.estado = "inicio"

        # Evaluación
        self.pregunta_actual = 0
        self.respuestas = []

        # Preguntas iniciales
        self.preguntas = [

            "¿Cómo te has sentido emocionalmente durante esta semana?",

            "¿Has tenido dificultades para dormir?",

            "¿Te has sentido muy estresado por la universidad?",

            "¿Has sentido ansiedad antes de clases o exámenes?",

            "¿Has perdido la motivación para estudiar?",

            "¿Cómo calificarías tu bienestar general del 1 al 5?"
        ]
    # =====================================================
    # BIENVENIDA
    # =====================================================

    def bienvenida(self):

        self.estado = "nombre"

        return {
            "mensaje":
            "🌿 Hola, soy OASIS.\n\n"
            "Tu aliado para el bienestar universitario.\n\n"
            "Antes de comenzar...\n\n"
            "¿Cómo te llamas?"
        }


    # =====================================================
    # GUARDAR NOMBRE
    # =====================================================

    def guardar_nombre(self, nombre):

        self.memoria.guardar_nombre(nombre)

        self.estado = "evaluacion"

        self.pregunta_actual = 0

        self.respuestas.clear()

        return {

            "mensaje":

            f"Mucho gusto, {nombre}. 😊\n\n"

            "Quisiera conocerte un poco mejor.\n\n"

            + self.preguntas[self.pregunta_actual]

        }
    # =====================================================
    # EVALUACIÓN INICIAL
    # =====================================================

    def evaluar(self, respuesta):

        self.respuestas.append(respuesta)

        self.pregunta_actual += 1

        # Aún quedan preguntas
        if self.pregunta_actual < len(self.preguntas):

            return {
                "mensaje": self.preguntas[self.pregunta_actual]
            }

        # Ya terminó la evaluación
        self.estado = "emocion"

        return {
            "mensaje":
            "💚 Muchas gracias por responder.\n\n"
            "Ahora cuéntame...\n\n"
            "¿Cómo te sientes hoy?"
        }