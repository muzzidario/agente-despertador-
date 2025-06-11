from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

mensajes_extra = [
    "Recordá respirar profundo antes de arrancar.",
        "Hoy puede ser un gran día.",
            "Ponete tu música favorita para empezar bien."
            ]

            @app.route("/", methods=["GET"])
            def mensaje():
                ahora = datetime.now()
                    dia = ahora.strftime("%A")
                        hora = ahora.strftime("%H:%M")
                            
                                saludo = f"Buen día, Dario. Hoy es {dia}, son las {hora}."
                                    extra = random.choice(mensajes_extra)
                                        
                                            respuesta = f"{saludo} {extra}"
                                                return jsonify({"mensaje": respuesta})