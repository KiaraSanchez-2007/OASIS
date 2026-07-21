"""
=========================================
MEMORIA CONVERSACIONAL
=========================================
"""

class Memoria:

    def __init__(self):

        self.historial = []

        self.nombre = None
        self.ultima_emocion = None
        self.ultima_tarea = None

    # ------------------------------------
    # HISTORIAL
    # ------------------------------------

    def guardar(self, usuario, respuesta):

        self.historial.append({

            "usuario": usuario,
            "respuesta": respuesta

        })

        if len(self.historial) > 20:
            self.historial.pop(0)

    # ------------------------------------
    # NOMBRE
    # ------------------------------------

    def guardar_nombre(self, nombre):

        self.nombre = nombre

    def obtener_nombre(self):

        return self.nombre

    # ------------------------------------
    # EMOCIÓN
    # ------------------------------------

    def guardar_emocion(self, emocion):

        self.ultima_emocion = emocion

    def obtener_emocion(self):

        return self.ultima_emocion

    # ------------------------------------
    # TAREA
    # ------------------------------------

    def guardar_tarea(self, tarea):

        self.ultima_tarea = tarea

    def obtener_tarea(self):

        return self.ultima_tarea

    # ------------------------------------
    # HISTORIAL
    # ------------------------------------

    def obtener_historial(self):

        return self.historial

    # ------------------------------------
    # LIMPIAR
    # ------------------------------------

    def limpiar(self):

        self.historial = []
        self.nombre = None
        self.ultima_emocion = None
        self.ultima_tarea = None