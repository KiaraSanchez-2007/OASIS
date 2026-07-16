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

# ==========================================
# VARIABLES DE ENTORNO
# ==========================================

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "OASIS_UTP_2026")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


# ==========================================
# WEB
# ==========================================

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


# ==========================================
# ENVIAR MENSAJE A WHATSAPP
# ==========================================

def enviar_mensaje(numero: str, mensaje: str):

    if not WHATSAPP_TOKEN:
        print("ERROR: WHATSAPP_TOKEN vacío")
        return

    if not PHONE_NUMBER_ID:
        print("ERROR: PHONE_NUMBER_ID vacío")
        return

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

    # ==========================
    # DEPURACIÓN
    # ==========================

    print("====================================")
    print("ENVIANDO MENSAJE A META")
    print("TOKEN:", WHATSAPP_TOKEN[:25], "...")
    print("PHONE_NUMBER_ID:", PHONE_NUMBER_ID)
    print("DESTINATARIO:", numero)
    print("URL:", url)
    print("MENSAJE:", mensaje)
    print("====================================")

    respuesta = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("Respuesta Meta:", respuesta.status_code)
    print(respuesta.text)


# ==========================================
# VERIFICAR WEBHOOK
# ==========================================

@app.get("/webhook")
async def verificar_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    print("Verificando webhook...")
    print("MODE:", mode)
    print("TOKEN:", token)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verificado correctamente")
        return PlainTextResponse(challenge)

    print("Error de verificación")
    return PlainTextResponse("Error", status_code=403)


# ==========================================
# RECIBIR MENSAJES
# ==========================================

@app.post("/webhook")
async def recibir_webhook(request: Request):

    body = await request.json()

    print("====================================")
    print("MENSAJE RECIBIDO DESDE WHATSAPP")
    print(body)
    print("====================================")

    try:

        if "entry" not in body:
            return {"status": "ok"}

        value = body["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return {"status": "ok"}

        mensaje = value["messages"][0]

        if mensaje["type"] != "text":
            print("Mensaje no es texto")
            return {"status": "ok"}

        numero = mensaje["from"]
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

        print("Respuesta del chatbot:", respuesta)

        enviar_mensaje(
            numero,
            str(respuesta)
        )

    except Exception as e:

        print("ERROR GENERAL")
        print(str(e))

    return {"status": "ok"}