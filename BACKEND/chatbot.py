from emociones import DetectorEmociones
from respiracion import Respiracion
from organizacion import Organizacion
from recursos import Recursos
from memoria import Memoria
from rutas.crisis import RutaCrisis
from evaluacion import Evaluacion


class OasisChatbot:

    def __init__(self):

        # -----------------------------
        # Módulos
        # -----------------------------

        self.detector = DetectorEmociones()
        self.respiracion = Respiracion()
        self.organizacion = Organizacion()
        self.recursos = Recursos()
        self.memoria = Memoria()
        self.ruta_crisis = RutaCrisis()
        self.evaluacion = Evaluacion()
        self.pregunta_actual = 1
        self.puntaje = 0

        # -----------------------------
        # Estado
        # -----------------------------

        self.estado = "inicio"

    # =====================================================
    # BIENVENIDA
    # =====================================================

    def bienvenida(self):

        self.estado = "bienvenida"

        return {
            "mensaje":
            "🌿 Hola, soy OASIS.\n\n"
            "Tu aliado para el bienestar universitario.\n\n"
            "Estoy aquí para ayudarte a manejar el estrés académico.\n\n"
            "¿Aceptas comenzar?\n\n"
            "1. Sí\n"
            "2. No"
        }

    # =====================================================
    # RESPUESTA A LA BIENVENIDA
    # =====================================================

    def responder_bienvenida(self, opcion):

        if opcion == "1":

            self.estado = "esperando_nombre"

            return {
                "mensaje":
                "😊 Excelente.\n\n"
                "Antes de comenzar...\n\n"
                "¿Cómo te llamas?"
            }

        elif opcion == "2":

            return {
                "mensaje":
                "Está bien.\n\n"
                "Cuando necesites hablar conmigo, aquí estaré. 💚"
            }

        else:

            return {
                "mensaje":
                "Por favor responde con 1 o 2."
            }

    # =====================================================
    # NOMBRE
    # =====================================================

    def guardar_nombre(self, nombre):

        self.memoria.guardar_nombre(nombre)
        self.estado = "menu_principal"

        print("ESTADO DESPUÉS DEL NOMBRE:", self.estado)

        return {
            "mensaje": (
                f"¡Mucho gusto, {nombre}! 😊\n\n"
                "¿En qué puedo ayudarte hoy?\n\n"
                "1️⃣ Ayuda en una situación de crisis\n"
                "2️⃣ Evaluar mi nivel de estrés\n"
                "3️⃣ Tips para organizar mis actividades"
        )
    }

    def menu_principal(self, opcion):

       print(">>> MENU PRINCIPAL <<<", opcion)

       if opcion == "1":
            self.estado = "crisis"
            return self.ruta_crisis.iniciar()

       elif opcion == "2":
            print(">>> OPCION 2 EJECUTADA <<<")

            self.estado = "evaluacion"
            self.pregunta_actual = 1
            self.puntaje = 0

            return {
                "mensaje":
                    f"📋 Pregunta 1 de {self.evaluacion.total_preguntas()}\n\n"
                    f"{self.evaluacion.obtener_pregunta(1)}\n\n"
                    "1️⃣ Nunca\n"
                    "2️⃣ Algunas veces\n"
                    "3️⃣ Frecuentemente\n"
                    "4️⃣ Siempre"
        }

       elif opcion == "3":
            self.estado = "esperando_tarea"
            return {
        "mensaje":
            "📅 Perfecto.\n\n"
            "Cuéntame, ¿qué actividad o tarea deseas organizar?"
    }

    def analizar_emocion(self, texto):

        emocion = self.detector.detectar(texto)

        self.memoria.guardar_emocion(emocion)

        nombre = self.memoria.obtener_nombre()

        # --------------------------------
        # ESTRÉS
        # --------------------------------

        if emocion == "estres":

            self.estado = "menu_estres"

            return {

                "mensaje":

                f"Entiendo, {nombre}. 💚\n\n"

                "Parece que estás experimentando estrés.\n\n"

                "¿Qué prefieres hacer?\n\n"

                "1️⃣ Ejercicio de respiración\n"

                "2️⃣ Organizar mis tareas\n"

                "3️⃣ Técnicas de estudio\n"

                "4️⃣ Hablar conmigo"
            }

        # --------------------------------
        # ANSIEDAD
        # --------------------------------

        elif emocion == "ansiedad":

            self.estado = "menu_ansiedad"

            return {

                "mensaje":

                f"Gracias por confiar en mí, {nombre}. 💙\n\n"

                "La ansiedad puede aparecer cuando tenemos muchas preocupaciones.\n\n"

                "¿Qué deseas hacer?\n\n"

                "1️⃣ Respiración 4-7-8\n"

                "2️⃣ Respiración profunda\n"

                "3️⃣ Conversar"
            }

        # --------------------------------
        # TRISTEZA
        # --------------------------------

        elif emocion == "tristeza":

            self.estado = "conversacion"

            return {

                "mensaje":

                f"Lo siento mucho, {nombre}. 💚\n\n"

                "Estoy aquí para escucharte.\n\n"

                "Cuéntame qué está ocurriendo."
            }

        # --------------------------------
        # FELICIDAD
        # --------------------------------

        elif emocion == "feliz":

            return {

                "mensaje":

                f"😊 Qué buena noticia, {nombre}.\n\n"

                "Me alegra saber que hoy te sientes bien.\n\n"

                + self.recursos.motivacion()
            }

        # --------------------------------
        # CANSANCIO
        # --------------------------------

        elif emocion == "cansancio":

            self.estado = "menu_cansancio"

            return {

                "mensaje":

                f"{nombre}, parece que estás bastante cansado.\n\n"

                "Recuerda que descansar también forma parte del aprendizaje.\n\n"

                "1️⃣ Respirar\n"

                "2️⃣ Consejos de estudio\n"

                "3️⃣ Motivación"
            }

        # --------------------------------
        # DESCONOCIDO
        # --------------------------------

        else:

            self.estado = "conversacion"

            return {

                "mensaje":

                "Gracias por compartir cómo te sientes.\n\n"

                "Cuéntame un poco más."
            }
    # =====================================================
    # MENÚ ESTRÉS
    # =====================================================

    def menu_estres(self, opcion):

        if opcion == "1":

            return {
                "mensaje": self.respiracion.ejercicio_basico()
            }

        elif opcion == "2":

            self.estado = "esperando_tarea"

            return {
                "mensaje":
                "📝 Cuéntame cuál es la tarea que más te preocupa."
            }

        elif opcion == "3":

            return {
                "mensaje": self.recursos.tecnicas_estudio()
            }

        elif opcion == "4":

            self.estado = "conversacion"

            return {
                "mensaje":
                "💚 Estoy aquí para escucharte.\n\nCuéntame qué está ocurriendo."
            }

        else:

            return {
                "mensaje":
                "Por favor escribe 1, 2, 3 o 4."
            }


    # =====================================================
    # MENÚ ANSIEDAD
    # =====================================================

    def menu_ansiedad(self, opcion):

        if opcion == "1":

            return {
                "mensaje": self.respiracion.respiracion_478()
            }

        elif opcion == "2":

            return {
                "mensaje": self.respiracion.respiracion_profunda()
            }

        elif opcion == "3":

            self.estado = "conversacion"

            return {
                "mensaje":
                "💙 Cuéntame con tranquilidad qué está pasando."
            }

        else:

            return {
                "mensaje":
                "Escribe 1, 2 o 3."
            }


    # =====================================================
    # MENÚ CANSANCIO
    # =====================================================

    def menu_cansancio(self, opcion):

        if opcion == "1":

            return {
                "mensaje": self.respiracion.ejercicio_basico()
            }

        elif opcion == "2":

            return {
                "mensaje": self.recursos.tecnicas_estudio()
            }

        elif opcion == "3":

            return {
                "mensaje": self.recursos.motivacion()
            }

        else:

            return {
                "mensaje":
                "Escribe 1, 2 o 3."
            }


    # =====================================================
    # CONVERSACIÓN
    # =====================================================

    def conversacion(self, mensaje):

        # Guardar en memoria
        self.memoria.guardar(mensaje, "")

        ultima_tarea = self.memoria.obtener_tarea()
        ultima_emocion = self.memoria.obtener_emocion()

        if ultima_tarea:

            return {
                "mensaje":
                    f"😊 Me alegra seguir conversando contigo.\n\n"
                    f"📌 La última tarea que registré fue:\n"
                    f"👉 {ultima_tarea}\n\n"
                    "¿Cómo vas con ella?"
            }

        if ultima_emocion:

            return {
                "mensaje":
                    f"💙 Recuerdo que anteriormente te sentías *{ultima_emocion}*.\n\n"
                    "¿Te sientes un poco mejor ahora?"
            }

        return {
            "mensaje":
                "💚 Gracias por confiar en mí.\n\n"
                "Estoy aquí para acompañarte cuando lo necesites."
        }

    def evaluar(self, opcion):

        print(">>> EVALUAR <<<", opcion)
        print("PREGUNTA ACTUAL ANTES:", self.pregunta_actual)
        print("PUNTAJE ANTES:", self.puntaje)

        opcion = opcion.strip()

        # Validar respuesta
        if opcion not in ["1", "2", "3", "4"]:
            return {
                "mensaje": "❌ Responde únicamente con 1, 2, 3 o 4."
            }

        # Acumular puntaje
        self.puntaje += int(opcion)

        # Siguiente pregunta
        self.pregunta_actual += 1

        print("PREGUNTA ACTUAL DESPUÉS:", self.pregunta_actual)
        print("TOTAL PREGUNTAS:", self.evaluacion.total_preguntas())

        # Si todavía hay preguntas
        if self.pregunta_actual <= self.evaluacion.total_preguntas():

            return {
                "mensaje":
                    f"📋 Pregunta {self.pregunta_actual} de {self.evaluacion.total_preguntas()}\n\n"
                    f"{self.evaluacion.obtener_pregunta(self.pregunta_actual)}\n\n"
                    "1️⃣ Nunca\n"
                    "2️⃣ Algunas veces\n"
                    "3️⃣ Frecuentemente\n"
                    "4️⃣ Siempre"
            }

        # Resultado final
        promedio = self.puntaje / self.evaluacion.total_preguntas()

        self.estado = "conversacion"

        if promedio <= 1.5:
            mensaje = "🟢 Tu nivel de estrés parece ser bajo. Sigue cuidando tu bienestar."

        elif promedio <= 2.5:
            mensaje = "🟡 Presentas un nivel moderado de estrés. Te recomiendo realizar pausas activas y ejercicios de respiración."

        else:
            mensaje = (
                "🔴 Detecto un nivel elevado de estrés. "
                "Te recomiendo conversar con Bienestar Universitario "
                "y practicar las técnicas que OASIS ofrece."
            )

        # Reiniciar evaluación
        self.pregunta_actual = 1
        self.puntaje = 0

        return {
            "mensaje": mensaje
        }


    def organizar_tarea(self, tarea):

        self.tarea_actual = tarea

        self.estado = "conversacion"

        return {
            "mensaje":
                "✅ He registrado tu tarea.\n\n"
                f"📌 Tarea: {tarea}\n\n"
                "Te recomiendo dividirla en estos pasos:\n\n"
                "1️⃣ Comprende qué debes hacer.\n"
                "2️⃣ Divide el trabajo en partes pequeñas.\n"
                "3️⃣ Comienza por la parte más sencilla.\n"
                "4️⃣ Descansa 5 a 10 minutos cada hora.\n"
                "5️⃣ Revisa tu trabajo antes de finalizar.\n\n"
                "💪 ¡Ánimo! Tú puedes lograrlo."
    }


    def conversar(self, mensaje):
        return self.conversacion(mensaje)


    def responder(self, texto):

        print("RESPONDER -> ESTADO:", self.estado, "| TEXTO:", texto)

        if self.estado == "inicio":
            return self.bienvenida()

        elif self.estado == "bienvenida":
            return self.responder_bienvenida(texto)

        elif self.estado == "esperando_nombre":
            return self.guardar_nombre(texto)

        elif self.estado == "menu_principal":
            return self.menu_principal(texto)

        elif self.estado == "crisis":
            return self.ruta_crisis.procesar(texto)

        elif self.estado == "evaluacion":
            return self.evaluar(texto)

        elif self.estado == "emocion":
            return self.analizar_emocion(texto)

        elif self.estado == "menu_estres":
            return self.menu_estres(texto)

        elif self.estado == "menu_ansiedad":
            return self.menu_ansiedad(texto)

        elif self.estado == "menu_cansancio":
            return self.menu_cansancio(texto)

        elif self.estado == "esperando_tarea":
            return self.organizar_tarea(texto)

        else:
            return self.conversacion(texto)    