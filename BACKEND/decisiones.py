"""
=========================================
OASIS DECISIONES
Motor de Decisiones Inteligente
Versión 3.0
=========================================
"""


class MotorDecisiones:

    def __init__(self):

        pass

    def decidir(self, recomendaciones):

        decisiones = []

        for recomendacion in recomendaciones:

            if recomendacion == "sugerir_tecnica":

                decisiones.append({
                    "accion": "mostrar_tecnicas"
                })

            elif recomendacion == "evitar_respiracion":

                decisiones.append({
                    "accion": "no_repetir_respiracion"
                })

            elif recomendacion == "seguimiento_emocional":

                decisiones.append({
                    "accion": "preguntar_como_sigue"
                })

            elif recomendacion == "recordar_tareas":

                decisiones.append({
                    "accion": "mostrar_tareas"
                })

        return decisiones