// ===============================
// OASIS 3.0
// ===============================

const chat = document.getElementById("chat");
const texto = document.getElementById("texto");
const boton = document.getElementById("enviar");

const URL = "http://127.0.0.1:8000/mensaje";

let escribiendo = false;
// ===============================
// Agregar mensajes al chat
// ===============================

function agregarMensaje(textoMensaje, tipo = "bot") {

    const mensaje = document.createElement("div");

    mensaje.className = tipo === "bot"
        ? "mensaje bot"
        : "mensaje usuario";

    const hora = new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit"
});

if(tipo === "bot"){

    mensaje.innerHTML =
        `<div class="nombre-bot">🌿 OASIS</div>` +
        textoMensaje.replace(/\n/g,"<br>") +
        `<div class="hora">${hora}</div>`;

}else{

    mensaje.innerHTML =
        textoMensaje.replace(/\n/g,"<br>") +
        `<div class="hora">${hora}</div>`;

}

    chat.appendChild(mensaje);

    bajarChat();

}
// ===============================
// Escribir mensaje letra por letra
// ===============================

async function escribirMensaje(textoMensaje){

    const mensaje = document.createElement("div");

    mensaje.className = "mensaje bot";

    chat.appendChild(mensaje);

    let textoActual = "";

    for(let i=0; i<textoMensaje.length; i++){

        textoActual += textoMensaje[i];

        const hora = new Date().toLocaleTimeString([],{
            hour:"2-digit",
            minute:"2-digit"
        });

        mensaje.innerHTML =
            textoActual.replace(/\n/g,"<br>") +
            `<div class="hora">${hora}</div>`;

        bajarChat();

        await new Promise(resolve => setTimeout(resolve,18));

    }

}
function bajarChat(){

    chat.scrollTo({

        top: chat.scrollHeight,

        behavior:"smooth"

    });

}

// ===============================
// Indicador escribiendo...
// ===============================

function mostrarEscribiendo() {

    if (escribiendo) return;

    escribiendo = true;

    const mensaje = document.createElement("div");

    mensaje.className = "mensaje bot";

    mensaje.id = "escribiendo";

    mensaje.innerHTML = `

<div class="nombre-bot">🌿 OASIS</div>

<div>Escribiendo...</div>

<div class="typing">

    <span></span>

    <span></span>

    <span></span>

</div>

`;

    chat.appendChild(mensaje);

    bajarChat();
}

function ocultarEscribiendo() {

    escribiendo = false;

    const mensaje = document.getElementById("escribiendo");

    if (mensaje) {

        mensaje.remove();

    }

}
// ===============================
// Enviar mensaje
// ===============================

async function enviarMensaje() {

    const mensaje = texto.value.trim();

    if (mensaje === "") return;

    agregarMensaje(mensaje, "usuario");

    texto.value = "";

    texto.focus();

    mostrarEscribiendo();

    try {

        const respuesta = await fetch(

            URL + "?texto=" + encodeURIComponent(mensaje)

        );

        const datos = await respuesta.json();

// pequeño retraso para simular que OASIS escribe
await new Promise(resolve => setTimeout(resolve, 1200));

ocultarEscribiendo();

await escribirMensaje(datos.mensaje);

    }

    catch(error){

        ocultarEscribiendo();

        agregarMensaje(

            "❌ No fue posible conectar con OASIS.",

            "bot"

        );

        console.error(error);

    }

}
// ===============================
// Eventos
// ===============================

// Botón Enviar
boton.addEventListener("click", enviarMensaje);

// Tecla Enter
texto.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {

        enviarMensaje();

    }

});

// ===============================
// Iniciar conversación
// ===============================

window.onload = async function () {

    try {

        const respuesta = await fetch(URL + "?texto=inicio");

        const datos = await respuesta.json();

        agregarMensaje(datos.mensaje, "bot");

    }

    catch (error) {

        console.error(error);

    }

};