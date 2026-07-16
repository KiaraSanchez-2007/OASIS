class Evaluacion:

    def __init__(self):

        self.preguntas = [

            {
                "id": 1,
                "texto": "¿Cómo te has sentido emocionalmente durante esta semana?"
            },

            {
                "id": 2,
                "texto": "¿Has tenido dificultades para dormir?"
            },

            {
                "id": 3,
                "texto": "¿Sientes mucha presión por las tareas o exámenes?"
            },

            {
                "id": 4,
                "texto": "¿Has perdido interés en actividades que antes disfrutabas?"
            },

            {
                "id": 5,
                "texto": "¿Te has sentido muy cansado aunque hayas descansado?"
            }

        ]

    def obtener_pregunta(self, numero):

        if numero <= len(self.preguntas):

            return self.preguntas[numero - 1]["texto"]

        return None

    def total_preguntas(self):

        return len(self.preguntas)