class RutaCrisis:

    def __init__(self):

        self.estado = "inicio"
        self.emocion = None

    # =====================================================
    # INICIO
    # =====================================================

    def iniciar(self):

        self.estado = "emocion"

        return {
            "mensaje":
                "🆘 *Ayuda en una situación de crisis*\n\n"
                "Lamento que estés pasando por un momento difícil. 💙\n\n"
                "Estoy aquí para acompañarte.\n\n"
                "¿Qué describe mejor cómo te sientes?\n\n"
                "1️⃣ Muy triste\n"
                "2️⃣ Muy ansioso\n"
                "3️⃣ Muy frustrado\n"
                "4️⃣ Agotado emocionalmente"
        }

    # =====================================================
    # CONTROLADOR
    # =====================================================

    def procesar(self, texto):

        texto = texto.strip()

        if self.estado == "emocion":
            return self.procesar_emocion(texto)

        elif self.estado == "situacion":
            return self.procesar_situacion(texto)

        elif self.estado == "tecnica":
            return self.procesar_tecnica(texto)

        return self.iniciar()

    # =====================================================
    # EMOCIONES
    # =====================================================

    def procesar_emocion(self, opcion):

        if opcion == "1":
            self.emocion = "triste"

        elif opcion == "2":
            self.emocion = "ansioso"

        elif opcion == "3":
            self.emocion = "frustrado"

        elif opcion == "4":
            self.emocion = "agotado"

        else:
            return {
                "mensaje":
                    "❌ Escribe únicamente 1, 2, 3 o 4."
            }

        self.estado = "situacion"

        return {
            "mensaje":
                "Gracias por confiar en mí. 💙\n\n"
                "¿Qué situación describe mejor lo que estás viviendo?\n\n"
                "1️⃣ Problemas académicos\n"
                "2️⃣ Problemas familiares\n"
                "3️⃣ Problemas de pareja\n"
                "4️⃣ Problemas económicos"
        }

    # =====================================================
    # SITUACIÓN
    # =====================================================

    def procesar_situacion(self, opcion):

        mensajes = {

            "1":
                "📚 Entiendo que la carga académica puede sentirse muy pesada.\n\n"
                "Recuerda que ningún examen define tu valor como persona.",

            "2":
                "🏠 Los conflictos familiares pueden generar mucho estrés.\n\n"
                "Busca un momento tranquilo para expresar cómo te sientes.",

            "3":
                "💜 Las relaciones personales pueden afectarnos profundamente.\n\n"
                "Permítete sentir tus emociones sin juzgarte.",

            "4":
                "💵 Las preocupaciones económicas generan mucha presión.\n\n"
                "No estás solo; muchas personas atraviesan situaciones similares."
        }

        if opcion not in mensajes:

            return {
                "mensaje":
                    "❌ Escribe únicamente 1, 2, 3 o 4."
            }

        self.estado = "tecnica"

        return {
            "mensaje":
                mensajes[opcion] +
                "\n\nAhora hagamos algo que pueda ayudarte.\n\n"
                "¿Qué prefieres?\n\n"
                "1️⃣ Respiración guiada\n"
                "2️⃣ Técnica 5-4-3-2-1\n"
                "3️⃣ Mensaje de apoyo\n"
                "4️⃣ Volver al menú"
        }

    # =====================================================
    # TÉCNICAS
    # =====================================================

    def procesar_tecnica(self, opcion):

        if opcion == "1":

            self.estado = "inicio"

            return {
                "mensaje":
                    "🌿 Respiración guiada\n\n"
                    "Inhala durante 4 segundos.\n"
                    "Mantén el aire 4 segundos.\n"
                    "Exhala lentamente durante 6 segundos.\n\n"
                    "Repite este ejercicio cinco veces.\n\n"
                    "Cuando termines, vuelve a escribirme."
            }

        elif opcion == "2":

            self.estado = "inicio"

            return {
                "mensaje":
                    "🌼 Técnica 5-4-3-2-1\n\n"
                    "👀 Observa 5 cosas.\n"
                    "✋ Toca 4 cosas.\n"
                    "👂 Escucha 3 sonidos.\n"
                    "👃 Identifica 2 olores.\n"
                    "👅 Percibe 1 sabor.\n\n"
                    "Esta técnica ayuda a disminuir la ansiedad."
            }

        elif opcion == "3":

            self.estado = "inicio"

            return {
                "mensaje":
                    "💙 Quiero recordarte algo importante.\n\n"
                    "Lo que estás viviendo no define quién eres.\n\n"
                    "Pedir ayuda demuestra fortaleza.\n\n"
                    "Confía en que este momento también pasará."
            }

        elif opcion == "4":

            self.estado = "inicio"

            return {
                "mensaje":
                    "🏠 Has regresado al menú principal.\n\n"
                    "Escribe:\n\n"
                    "1️⃣ Crisis\n"
                    "2️⃣ Evaluación de estrés\n"
                    "3️⃣ Organización de actividades"
            }

        return {
            "mensaje":
                "❌ Escribe únicamente 1, 2, 3 o 4."
        }