"""
=========================================
MOTOR DE DECISIONES
OASIS v4.0
=========================================
"""

class MotorDecisiones:

    def decidir(self, contexto):

        decisiones = {

            "usar_nombre": contexto.get("recordar_nombre", False),

            "usar_emocion": contexto.get("recordar_emocion", False),

            "usar_tarea": contexto.get("recordar_tarea", False)

        }

        return decisiones