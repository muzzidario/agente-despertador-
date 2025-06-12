from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

mensajes_extra = [
    "Recordá respirar profundo antes de arrancar.",
    "Hoy puede ser un gran día.",
    "Ponete tu música favorita para empezar bien."
]

@app.route("/", methods=["GET"])
def mensaje():
    ahora = (datetime.utcnow() - timedelta(hours=3)).time
    dia = ahora.strftime("%A")
    hora = ahora.strftime("%H:%M")

    saludo = f"Buen día, Dario. Hoy es {dia}, son las {hora}."
    extra = random.choice(mensajes_extra)

    respuesta = f"{saludo} {extra}"
    return jsonify({"mensaje": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
