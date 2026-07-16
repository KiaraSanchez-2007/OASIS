"""
=========================================
OASIS ENGINE
Motor Conversacional Oficial
Versión 3.0
=========================================
"""

from chatbot import OasisChatbot
from intencion import DetectorIntencion
from contexto import GestorContexto
from decisiones import MotorDecisiones
from adaptador import AdaptadorConversacion


class OasisEngine:

    def __init__(self):

        # Chatbot principal
        self.chatbot = OasisChatbot()

        # Motor de IA
        self.detector = DetectorIntencion()
        self.contexto = GestorContexto()
        self.decisiones = MotorDecisiones()
        self.adaptador = AdaptadorConversacion()

        # Rutas
        self.rutas = {
            "inicio": self.chatbot.bienvenida,
            "nombre": self.chatbot.guardar_nombre,
            "evaluacion": self.chatbot.evaluar,
            "emocion": self.chatbot.analizar_emocion,
            "menu_estres": self.chatbot.menu_estres,
            "esperando_tarea": self.chatbot.organizar_tarea,
            "menu_ansiedad": self.chatbot.menu_ansiedad,
            "menu_cansancio": self.chatbot.menu_cansancio,
            "conversacion": self.chatbot.conversar
        }

    def procesar(self, texto):

        texto = texto.strip()

        intencion = self.detector.detectar(texto)
        print("INTENCIÓN:", intencion)

        recomendaciones = self.contexto.analizar(
            self.chatbot.memoria
        )

        print("CONTEXTO:", recomendaciones)

        decisiones = self.decisiones.decidir(
            recomendaciones
        )

        self.adaptador.aplicar(
            self.chatbot,
            decisiones
        )

        print("DECISIONES:", decisiones)

        estado = self.chatbot.estado

        if estado == "inicio":
            return self.chatbot.bienvenida()

        return self.chatbot.responder(texto)