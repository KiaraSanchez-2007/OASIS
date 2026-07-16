from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

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

# Token para verificar el webhook con Meta
VERIFY_TOKEN = "OASIS_UTP_2026"


# ==========================
# WEB
# ==========================

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


# ==========================
# WEBHOOK WHATSAPP
# ==========================

@app.get("/webhook")
async def verificar_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Error", status_code=403)


@app.post("/webhook")
async def recibir_webhook(request: Request):

    body = await request.json()

    print("Mensaje recibido desde WhatsApp:")
    print(body)

    return {"status": "ok"}