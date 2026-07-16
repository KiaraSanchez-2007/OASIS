"""
=========================================
ADAPTADOR DE CONVERSACIÓN
=========================================
"""

class AdaptadorConversacion:

    def aplicar(self, chatbot, decisiones):

        for decision in decisiones:

            accion = decision["accion"]

            if accion == "no_repetir_respiracion":
                chatbot.respiracion_repetida = True

            elif accion == "mostrar_tareas":
                chatbot.recordar_tareas = True

            elif accion == "preguntar_como_sigue":
                chatbot.seguimiento = True

            elif accion == "mostrar_tecnicas":
                chatbot.sugerir_tecnicas = True