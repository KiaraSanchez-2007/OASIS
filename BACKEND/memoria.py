class Memoria:

    def __init__(self):

        # Datos del usuario
        self.nombre = ""
        self.carrera = ""
        self.universidad = ""

        # Estado emocional
        self.nivel_estres = 0

        # Historial
        self.emociones = []
        self.intenciones = []
        self.tareas = []
        self.tecnicas_utilizadas = []
        self.conversacion = []

        # Estadísticas
        self.fecha_ultima_conversacion = ""
        self.total_conversaciones = 0

    # ======================================
    # DATOS PERSONALES
    # ======================================

    def guardar_nombre(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def guardar_carrera(self, carrera):
        self.carrera = carrera

    def obtener_carrera(self):
        return self.carrera

    def guardar_universidad(self, universidad):
        self.universidad = universidad

    def obtener_universidad(self):
        return self.universidad

    # ======================================
    # NIVEL DE ESTRÉS
    # ======================================

    def guardar_nivel_estres(self, nivel):
        self.nivel_estres = nivel

    def obtener_nivel_estres(self):
        return self.nivel_estres

    # ======================================
    # EMOCIONES
    # ======================================

    def guardar_emocion(self, emocion):
        self.emociones.append(emocion)

    def obtener_emociones(self):
        return self.emociones

    def ultima_emocion(self):
        if self.emociones:
            return self.emociones[-1]
        return None

    # ======================================
    # INTENCIONES
    # ======================================

    def guardar_intencion(self, intencion):
        self.intenciones.append(intencion)

    def obtener_intenciones(self):
        return self.intenciones

    def ultima_intencion(self):
        if self.intenciones:
            return self.intenciones[-1]
        return None

    # ======================================
    # TAREAS
    # ======================================

    def guardar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas

    # ======================================
    # TÉCNICAS
    # ======================================

    def guardar_tecnica(self, tecnica):

        if tecnica not in self.tecnicas_utilizadas:
            self.tecnicas_utilizadas.append(tecnica)

    def obtener_tecnicas(self):
        return self.tecnicas_utilizadas

    def ultima_tecnica(self):

        if self.tecnicas_utilizadas:
            return self.tecnicas_utilizadas[-1]

        return None

    # ======================================
    # CONVERSACIÓN
    # ======================================

    def guardar_mensaje(self, usuario, mensaje):

        self.conversacion.append({
            "usuario": usuario,
            "mensaje": mensaje
        })

        self.total_conversaciones += 1

    def obtener_conversacion(self):
        return self.conversacion

    def ultimo_mensaje(self):

        if self.conversacion:
            return self.conversacion[-1]

        return None

    # ======================================
    # ESTADÍSTICAS
    # ======================================

    def total_mensajes(self):
        return len(self.conversacion)

    # ======================================
    # REINICIAR
    # ======================================

    def limpiar(self):

        self.nombre = ""
        self.carrera = ""
        self.universidad = ""

        self.nivel_estres = 0

        self.emociones.clear()
        self.intenciones.clear()
        self.tareas.clear()
        self.tecnicas_utilizadas.clear()
        self.conversacion.clear()

        self.fecha_ultima_conversacion = ""
        self.total_conversaciones = 0