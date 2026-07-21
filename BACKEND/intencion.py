class DetectorIntencion:

    def __init__(self):

        self.categorias = {

            "crisis": [

                # Tristeza
                "triste",
                "llorar",
                "lloro",
                "deprimido",
                "deprimida",
                "vacío",
                "vacio",
                "solo",
                "sola",
                "desanimado",
                "desanimada",
                "sin ganas",

                # Ansiedad
                "ansiedad",
                "ansioso",
                "ansiosa",
                "nervioso",
                "nerviosa",
                "desesperado",
                "desesperada",
                "pánico",
                "panico",
                "ataque",
                "respirar",

                # Estrés intenso
                "estresado",
                "estresada",
                "colapsé",
                "colapse",
                "agotado",
                "agotada",
                "no puedo más",
                "no doy más",
                "no doy mas",

                # Frustración
                "frustrado",
                "frustrada",
                "fracaso",
                "rendirme",
                "rendirme",
                "todo me sale mal",
                "ya no puedo",

                # Riesgo
                "no quiero vivir",
                "me quiero morir",
                "quiero desaparecer"
            ],

            "organizacion": [

                "tarea",
                "tareas",
                "trabajo",
                "proyecto",
                "organizar",
                "agenda",
                "cronograma",
                "estudiar",
                "examen",
                "informe",
                "tiempo"
            ]
        }

    def detectar(self, texto):

        texto = texto.lower()

        # Buscar crisis
        for palabra in self.categorias["crisis"]:

            if palabra in texto:
                return "crisis"

        # Buscar organización
        for palabra in self.categorias["organizacion"]:

            if palabra in texto:
                return "organizacion"

        return "normal"