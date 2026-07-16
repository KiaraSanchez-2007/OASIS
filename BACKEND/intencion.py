class DetectorIntencion:

    def detectar(self, texto: str):

        texto = texto.lower().strip()

        if any(p in texto for p in [
            "estres",
            "estresado",
            "estresada",
            "presion",
            "agobiado",
            "agobiada"
        ]):
            return "estres"

        if any(p in texto for p in [
            "ansiedad",
            "ansioso",
            "ansiosa",
            "nervioso",
            "nerviosa",
            "miedo"
        ]):
            return "ansiedad"

        if any(p in texto for p in [
            "cansado",
            "cansada",
            "fatiga",
            "agotado",
            "agotada"
        ]):
            return "cansancio"

        return "general"