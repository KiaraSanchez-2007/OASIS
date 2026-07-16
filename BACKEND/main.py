import os
import requests

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

# ==========================
# VARIABLES DE ENTORNO
# ==========================

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "OASIS_UTP_2026")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


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
# ENVIAR MENSAJE A WHATSAPP
# ==========================

def enviar_mensaje(numero: str, mensaje: str):

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {
            "body": mensaje
        }
    }

    respuesta = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("Respuesta Meta:", respuesta.status_code)
    print(respuesta.text)


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

    try:

        if "entry" not in body:
            return {"status": "ok"}

        value = body["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return {"status": "ok"}

        mensaje = value["messages"][0]

        numero = mensaje["from"]

        texto = ""

        if mensaje["type"] == "text":
            texto = mensaje["text"]["body"]

        print("Número:", numero)
        print("Texto:", texto)

        respuesta = engine.procesar(texto)

        if isinstance(respuesta, dict):

            if "respuesta" in respuesta:
                respuesta = respuesta["respuesta"]

            elif "mensaje" in respuesta:
                respuesta = respuesta["mensaje"]

            else:
                respuesta = str(respuesta)

        enviar_mensaje(numero, str(respuesta))

    except Exception as e:

        print("ERROR:", str(e))

    return {"status": "ok"}