from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engine import OasisEngine

app = FastAPI(
    title="OASIS",
    description="Chatbot Inteligente para Bienestar Universitario",
    version="3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = OasisEngine()


@app.get("/")
def inicio():

    return {
        "proyecto": "OASIS",
        "estado": "Servidor funcionando correctamente"
    }


@app.get("/mensaje")
def mensaje(texto: str = ""):

    if texto.lower() == "inicio":

        engine.chatbot.memoria.limpiar()

        engine.chatbot.estado = "inicio"

        engine.chatbot.pregunta_actual = 1

    return engine.procesar(texto)