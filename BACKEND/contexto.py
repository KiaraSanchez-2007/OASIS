"""
=========================================
OASIS CONTEXTO
Gestor de Contexto Conversacional
Versión 3.0
=========================================
"""


class GestorContexto:

    def __init__(self):

        pass

    def analizar(self, memoria):

        recomendaciones = []

        # Si nunca realizó una técnica
        if len(memoria.obtener_tecnicas()) == 0:

            recomendaciones.append(
                "sugerir_tecnica"
            )

        # Si ya hizo respiración
        if "Respiración básica" in memoria.obtener_tecnicas():

            recomendaciones.append(
                "evitar_respiracion"
            )

        # Si tiene muchas emociones registradas
        if len(memoria.emociones) >= 3:

            recomendaciones.append(
                "seguimiento_emocional"
            )

        # Si tiene tareas pendientes
        if len(memoria.obtener_tareas()) > 0:

            recomendaciones.append(
                "recordar_tareas"
            )

        return recomendaciones