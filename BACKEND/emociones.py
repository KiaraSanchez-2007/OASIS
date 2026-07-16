class DetectorEmociones:

    def detectar(self, texto):

        texto = texto.lower().strip()

        emociones = {

            "estres": [
                "estres",
                "estrés",
                "estresado",
                "estresada",
                "agobiado",
                "agobiada",
                "presionado",
                "presionada",
                "saturado",
                "saturada",
                "abrumado",
                "abrumada",
                "mucho trabajo",
                "demasiadas tareas",
                "no me alcanza el tiempo",
                "no puedo con todo"
            ],

            "ansiedad": [
                "ansiedad",
                "ansioso",
                "ansiosa",
                "nervioso",
                "nerviosa",
                "miedo",
                "preocupado",
                "preocupada",
                "desesperado",
                "desesperada",
                "no puedo dormir",
                "me preocupa",
                "me siento inseguro",
                "me siento insegura"
            ],

            "tristeza": [
                "triste",
                "tristeza",
                "deprimido",
                "deprimida",
                "desanimado",
                "desanimada",
                "vacío",
                "vacía",
                "solo",
                "sola",
                "llorar",
                "quiero llorar",
                "sin ánimo",
                "desmotivado",
                "desmotivada"
            ],

            "cansancio": [
                "cansado",
                "cansada",
                "agotado",
                "agotada",
                "fatiga",
                "sin energía",
                "no tengo fuerzas",
                "muy cansado",
                "muy cansada",
                "me quiero dormir",
                "no he dormido",
                "estoy exhausto",
                "estoy exhausta"
            ],

            "feliz": [
                "feliz",
                "contento",
                "contenta",
                "alegre",
                "motivado",
                "motivada",
                "emocionado",
                "emocionada",
                "excelente",
                "genial",
                "muy bien",
                "todo bien",
                "estoy bien"
            ]

        }

        for emocion, palabras in emociones.items():

            for palabra in palabras:

                if palabra in texto:
                    return emocion

        return "desconocido"