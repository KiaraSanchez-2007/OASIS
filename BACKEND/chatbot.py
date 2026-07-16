from evaluacion import Evaluacion
from memoria import Memoria
from emociones import DetectorEmociones
from organizacion import Organizacion
from respiracion import Respiracion
from recursos import Recursos
from database import BaseDatos


class OasisChatbot:

    def __init__(self):

        # Estado actual del chatbot
        self.estado = "inicio"

        # Módulos del chatbot
        self.evaluacion = Evaluacion()
        self.memoria = Memoria()
        self.db = BaseDatos()
        self.emociones = DetectorEmociones()
        self.organizacion = Organizacion()
        self.respiracion = Respiracion()
        self.recursos = Recursos()

        # Inteligencia contextual
        self.respiracion_repetida = False
        self.recordar_tareas = False
        self.seguimiento = False
        self.sugerir_tecnicas = False

        # Control de preguntas
        self.pregunta_actual = 1

    # --------------------------------------------------
    # Bienvenida
    # --------------------------------------------------

    def bienvenida(self):

        self.estado = "nombre"

        return {
            "mensaje":
                "🌿 Hola.\n\n"
                "Soy OASIS, tu asistente virtual de bienestar universitario.\n\n"
                "Estoy aquí para ayudarte a gestionar el estrés, la ansiedad y la organización de tus actividades académicas.\n\n"
                "Antes de comenzar me gustaría conocerte.\n\n"
                "¿Cuál es tu nombre?"
        }

    # --------------------------------------------------
    # Guardar nombre
    # --------------------------------------------------

    def guardar_nombre(self, nombre):

        print("ENTRÓ A guardar_nombre")
        print(nombre)

        nombre = nombre.strip()

        if nombre == "":
            return {
                "mensaje": "Por favor escribe tu nombre."
            }

        self.memoria.guardar_nombre(nombre)

        self.estado = "evaluacion"
        self.pregunta_actual = 1

        return {
            "mensaje":
                f"Mucho gusto, {nombre}. 😊\n\n"
                "Voy a hacerte cinco preguntas para conocerte mejor.\n\n"
                "No existen respuestas correctas o incorrectas.\n\n"
                f"Pregunta 1 de {self.evaluacion.total_preguntas()}\n\n"
                f"{self.evaluacion.obtener_pregunta(1)}"
        }

    # --------------------------------------------------
    # Evaluación
    # --------------------------------------------------

    def evaluar(self, respuesta):

        self.memoria.guardar_mensaje("usuario", respuesta)

        total = self.evaluacion.total_preguntas()

        if self.pregunta_actual < total:

            self.pregunta_actual += 1

            return {

                "mensaje":

                f"Pregunta {self.pregunta_actual} de {total}\n\n"

                f"{self.evaluacion.obtener_pregunta(self.pregunta_actual)}"

            }

        self.estado = "emocion"

        return {

            "mensaje":

            "💚 Gracias por responder todas las preguntas.\n\n"

            "Ahora cuéntame con tus propias palabras...\n\n"

            "¿Cómo te has sentido hoy?"

        }

    # --------------------------------------------------
    # Analizar emoción
    # --------------------------------------------------

    def analizar_emocion(self, texto):

        emocion = self.emociones.detectar(texto)

        self.memoria.guardar_mensaje("usuario", texto)

        self.memoria.guardar_emocion(emocion)

        if emocion == "estres":

            self.estado = "menu_estres"

            return {

                "mensaje":

                "😟 Detecté que podrías estar experimentando estrés.\n\n"

                "¿Qué te gustaría hacer?\n\n"

                "1️⃣ Ejercicio de respiración\n"

                "2️⃣ Organizar una tarea\n"

                "3️⃣ Técnicas de estudio\n"

                "4️⃣ Conversar"

            }

        elif emocion == "ansiedad":

            self.estado = "menu_ansiedad"

            return {

                "mensaje":

                "😰 Detecté que podrías estar sintiendo ansiedad.\n\n"

                "¿Qué deseas hacer?\n\n"

                "1️⃣ Respiración 4-7-8\n"

                "2️⃣ Buscar apoyo psicológico\n"

                "3️⃣ Conversar"

            }

        elif emocion == "cansancio":

            self.estado = "menu_cansancio"

            return {

                "mensaje":

                "😴 Detecté que podrías estar muy cansado.\n\n"

                "¿Qué deseas hacer?\n\n"

                "1️⃣ Respiración profunda\n"

                "2️⃣ Mensaje de motivación\n"

                "3️⃣ Técnicas de estudio"

            }

        elif emocion == "feliz":

            self.estado = "conversacion"

            return {

                "mensaje":

                "😊 Me alegra mucho saber que te sientes bien.\n\n"

                "Espero que continúes así.\n\n"

                "Recuerda que siempre puedes volver cuando necesites apoyo."

            }

        else:

            self.estado = "conversacion"

            return {

                "mensaje":

                "Gracias por contarme cómo te sientes.\n\n"

                "Estoy aquí para escucharte."

            }
                # --------------------------------------------------
    # Menú estrés
    # --------------------------------------------------

    def menu_estres(self, opcion):

        opcion = opcion.strip()

        if opcion == "1":

            self.estado = "conversacion"

            self.memoria.guardar_tecnica("Respiración básica")

            return {

                "mensaje": self.respiracion.ejercicio_basico()

            }

        elif opcion == "2":

            self.estado = "esperando_tarea"

            return {

                "mensaje":

                "📝 Cuéntame cuál es la tarea o actividad que deseas organizar."

            }

        elif opcion == "3":

            self.estado = "conversacion"

            return {

                "mensaje":

                self.recursos.tecnicas_estudio()

            }

        elif opcion == "4":

            self.estado = "conversacion"

            self.memoria.guardar_tecnica("Conversación guiada")

            return {

                "mensaje":

                "💚 Claro. Estoy aquí para escucharte.\n\n"

                "Cuéntame qué está pasando."

            }

        else:

            return {

                "mensaje":

                "Por favor elige una opción del 1 al 4."

            }
                # --------------------------------------------------
    # Organizar tarea
    # --------------------------------------------------

    def organizar_tarea(self, tarea):

        tarea = tarea.strip()

        if tarea == "":

            return {

                "mensaje":

                "Por favor escribe la tarea que deseas organizar."

            }

        self.memoria.guardar_tarea(tarea)

        self.estado = "conversacion"

        return {

            "mensaje":

            self.organizacion.prioridad(tarea)

        }
            # --------------------------------------------------
    # Menú ansiedad
    # --------------------------------------------------

    def menu_ansiedad(self, opcion):

        opcion = opcion.strip()

        if opcion == "1":

            self.estado = "conversacion"

            return {

                "mensaje":

                self.respiracion.respiracion_478()

            }

        elif opcion == "2":

            self.estado = "conversacion"

            self.memoria.guardar_tecnica("Organización de tareas")

            return {

                "mensaje":

                self.recursos.apoyo_psicologico()

            }

        elif opcion == "3":

            self.estado = "conversacion"

            self.memoria.guardar_tecnica("Técnicas de estudio")

            return {

                "mensaje":

                "💚 Gracias por confiar en mí.\n\n"

                "Puedes contarme con tranquilidad qué está ocurriendo."

            }

        else:

            return {

                "mensaje":

                "Por favor selecciona una opción del 1 al 3."

            }
                # --------------------------------------------------
    # Menú cansancio
    # --------------------------------------------------

    def menu_cansancio(self, opcion):

        opcion = opcion.strip()

        if opcion == "1":

            self.estado = "conversacion"

            return {

                "mensaje":

                self.respiracion.respiracion_profunda()

            }

        elif opcion == "2":

            self.estado = "conversacion"

            return {

                "mensaje":

                self.recursos.motivacion()

            }

        elif opcion == "3":

            self.estado = "conversacion"

            return {

                "mensaje":

                self.recursos.tecnicas_estudio()

            }

        else:

            return {

                "mensaje":

                "Por favor selecciona una opción del 1 al 3."

            }
                # --------------------------------------------------
    # Conversación libre
    # --------------------------------------------------

    def conversar(self, texto):

        texto = texto.strip()

        if texto == "":

            return {
                "mensaje": "Estoy aquí para escucharte. ¿Qué te gustaría contarme?"
            }

        self.memoria.guardar_mensaje("usuario", texto)
        self.db.guardar_mensaje("usuario", texto)

        if self.seguimiento:

            self.seguimiento = False

            respuesta = (
                "💚 Me alegra volver a hablar contigo.\n\n"
                "La última vez noté que estabas pasando por un momento difícil.\n\n"
                "¿Cómo te has sentido desde entonces?"
            )

            self.memoria.guardar_mensaje("oasis", respuesta)
            self.db.guardar_mensaje("oasis", respuesta)

            return {
                "mensaje": respuesta
            }

        if self.recordar_tareas:

            self.recordar_tareas = False

            tareas = self.memoria.obtener_tareas()

            if tareas:

                respuesta = (
                    f"📝 Recuerdo que tenías pendiente:\n\n"
                    f"• {tareas[-1]}\n\n"
                    "¿Lograste avanzar con esa actividad?"
                )

                self.memoria.guardar_mensaje("oasis", respuesta)
                self.db.guardar_mensaje("oasis", respuesta)

                return {
                    "mensaje": respuesta
                }

        if self.sugerir_tecnicas:

            self.sugerir_tecnicas = False

            respuesta = (
                "🌿 Ya utilizaste algunas técnicas anteriormente.\n\n"
                "Hoy podemos probar una diferente."
            )

            self.memoria.guardar_mensaje("oasis", respuesta)
            self.db.guardar_mensaje("oasis", respuesta)

            return {
                "mensaje": respuesta
            }

        nombre = self.memoria.obtener_nombre()

        emocion = self.memoria.ultima_emocion()

        if emocion == "estres":

            respuesta = (
                f"💚 Gracias por confiar en mí, {nombre}.\n\n"
                "Entiendo que el estrés puede hacer que todo parezca más difícil.\n\n"
                "Recuerda avanzar paso a paso. Estoy aquí para ayudarte."
            )

        elif emocion == "ansiedad":

            respuesta = (
                f"💚 Gracias por contarme cómo te sientes, {nombre}.\n\n"
                "La ansiedad puede sentirse muy intensa, pero no tienes que enfrentarla solo.\n\n"
                "Podemos trabajar juntos para que te sientas mejor."
            )

        elif emocion == "tristeza":

            respuesta = (
                f"💚 Gracias por abrirte conmigo, {nombre}.\n\n"
                "Lamento que estés pasando por este momento.\n\n"
                "Hablar de lo que sentimos también es una forma de cuidarnos."
            )

        elif emocion == "cansancio":

            respuesta = (
                f"💚 Entiendo, {nombre}.\n\n"
                "El cansancio también necesita atención.\n\n"
                "Recuerda descansar cuando sea posible y cuidar de ti."
            )

        elif emocion == "feliz":

            respuesta = (
                f"😊 Me alegra mucho saber que te sientes bien, {nombre}.\n\n"
                "Espero que ese ánimo te acompañe durante el día.\n\n"
                "Aquí estaré siempre que necesites conversar."
            )

        else:

            respuesta = (
                f"💚 Gracias por compartir conmigo, {nombre}.\n\n"
                "Estoy aquí para escucharte y acompañarte en lo que necesites."
            )

        self.memoria.guardar_mensaje("oasis", respuesta)
        self.db.guardar_mensaje("oasis", respuesta)

        return {
            "mensaje": respuesta
        }

    # --------------------------------------------------
    # Procesar mensajes
    # --------------------------------------------------

    def responder(self, texto):

        if self.estado == "inicio":
            return self.bienvenida()

        elif self.estado == "nombre":
            return self.guardar_nombre(texto)

        elif self.estado == "evaluacion":
            return self.evaluar(texto)

        elif self.estado == "emocion":
            return self.analizar_emocion(texto)

        elif self.estado == "menu_estres":
            return self.menu_estres(texto)

        elif self.estado == "esperando_tarea":
            return self.organizar_tarea(texto)

        elif self.estado == "menu_ansiedad":
            return self.menu_ansiedad(texto)

        elif self.estado == "menu_cansancio":
            return self.menu_cansancio(texto)

        elif self.estado == "conversacion":
            return self.conversar(texto)

        return {
            "mensaje": "No entendí tu mensaje."
        }