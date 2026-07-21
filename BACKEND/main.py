import os
import requests

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from engine import OasisEngine

# ==========================================
# FASTAPI
# ==========================================

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
# RUTA PRINCIPAL
# ==========================================

@app.get("/")
def inicio():
    return {
        "proyecto": "OASIS",
        "estado": "Servidor funcionando correctamente"
    }

# ==========================================
# PRUEBA WEB
# ==========================================

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

    print("\n==============================")
    print("ENVIANDO MENSAJE A META")
    print("==============================")
    print("URL:", url)
    print("PHONE_NUMBER_ID:", PHONE_NUMBER_ID)

    if WHATSAPP_TOKEN:
        print("TOKEN:", WHATSAPP_TOKEN[:20] + "...")
    else:
        print("TOKEN: NO ENCONTRADO")

    print("DESTINO:", numero)
    print("MENSAJE:", mensaje)

    respuesta = requests.post(
        url,
        headers=headers,
        json=data
    )

    print("\n====== RESPUESTA META ======")
    print("STATUS:", respuesta.status_code)
    print(respuesta.text)
    print("============================\n")

# ==========================================
# VERIFICAR WEBHOOK
# ==========================================

@app.get("/webhook")
async def verificar_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    print("\nVerificando Webhook")
    print("MODE:", mode)
    print("TOKEN:", token)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verificado correctamente.")
        return PlainTextResponse(challenge)

    print("Error de verificación.")
    return PlainTextResponse("Error", status_code=403)

# ==========================================
# RECIBIR MENSAJES
# ==========================================

@app.post("/webhook")
async def recibir_webhook(request: Request):

    body = await request.json()

    print("\n==============================")
    print("MENSAJE RECIBIDO DESDE WHATSAPP")
    print("==============================")
    print(body)

    try:

        if "entry" not in body:
            return {"status": "ok"}

        value = body["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            print("No llegaron mensajes.")
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

        print("Respuesta del chatbot:", respuesta)

        enviar_mensaje(
            numero,
            str(respuesta)
        )

    except Exception as e:

        print("\n========== ERROR GENERAL ==========")
        print(str(e))
        print("===================================\n")

    return {"status": "ok"}