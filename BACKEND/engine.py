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

        # Estados compatibles con chatbot.py
        self.rutas = {
        "inicio": self.chatbot.bienvenida,
        "bienvenida": self.chatbot.responder_bienvenida,
        "esperando_nombre": self.chatbot.guardar_nombre,
        "emocion": self.chatbot.analizar_emocion,
        "menu_estres": self.chatbot.menu_estres,
        "menu_ansiedad": self.chatbot.menu_ansiedad,
        "menu_cansancio": self.chatbot.menu_cansancio,
        "esperando_tarea": self.chatbot.organizar_tarea,
        "conversacion": self.chatbot.conversar
}

    def procesar(self, texto):

        texto = texto.strip()

        intencion = self.detector.detectar(texto)
        print("INTENCIÓN:", intencion)

        # ==========================================
        # DETECCIÓN AUTOMÁTICA DE CRISIS
        # ==========================================
        if intencion == "crisis" and self.chatbot.estado != "crisis":

            print(">>> CRISIS DETECTADA AUTOMÁTICAMENTE <<<")

            self.chatbot.estado = "crisis"

            return self.chatbot.ruta_crisis.iniciar()
            
        if intencion == "organizacion" and self.chatbot.estado != "esperando_tarea":

            print(">>> ORGANIZACIÓN DETECTADA AUTOMÁTICAMENTE <<<")

            self.chatbot.estado = "esperando_tarea"

            return {
                "mensaje":
                    "📅 Detecté que necesitas ayuda para organizar una actividad.\n\n"
                    "Cuéntame cuál es la tarea o actividad que deseas organizar."
    }

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

        print("ESTADO ACTUAL:", estado)

        if estado == "inicio":
            return self.chatbot.bienvenida()

        return self.chatbot.responder(texto)