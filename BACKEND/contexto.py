"""
=========================================
GESTOR DE CONTEXTO
OASIS v4.0
=========================================
"""

class GestorContexto:

    def analizar(self, memoria):

        recomendaciones = {
            "recordar_nombre": False,
            "recordar_emocion": False,
            "recordar_tarea": False
        }

        try:

            if hasattr(memoria, "obtener_nombre"):

                if memoria.obtener_nombre():
                    recomendaciones["recordar_nombre"] = True

            if memoria.obtener_emocion():
                recomendaciones["recordar_emocion"] = True

            if memoria.obtener_tarea():
                recomendaciones["recordar_tarea"] = True

        except Exception as e:

            print("ERROR CONTEXTO:", e)

        return recomendaciones