"""
=========================================
ADAPTADOR CONVERSACIONAL
OASIS v4.0
=========================================
"""

class AdaptadorConversacion:

    def aplicar(self, chatbot, decisiones):

        chatbot.usar_nombre = decisiones.get("usar_nombre", False)

        chatbot.usar_emocion = decisiones.get("usar_emocion", False)

        chatbot.usar_tarea = decisiones.get("usar_tarea", False)