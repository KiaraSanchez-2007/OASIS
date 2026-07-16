from emociones import DetectorEmociones
from respiracion import Respiracion
from organizacion import Organizacion
from recursos import Recursos
from memoria import Memoria


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

        self.estado = "emocion"

        return {

            "mensaje":

            f"Mucho gusto, {nombre}. 😊\n\n"

            "¿Cómo te has sentido hoy?"
        }
    # =====================================================
    # DETECCIÓN DE EMOCIONES
    # =====================================================

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

        self.memoria.guardar_mensaje("usuario", mensaje)

        return {
            "mensaje":
            "💚 Gracias por confiar en mí.\n\n"
            "Entiendo cómo te sientes.\n\n"
            "Estoy aquí para acompañarte."
        }            