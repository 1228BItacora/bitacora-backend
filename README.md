from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Clave API conectada con OpenAI
openai.api_key = "sk-proj-CZSEH6AbqYA"

@app.route("/")
def inicio():
    return "Servidor conectado con OpenAI."

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    if not mensaje:
        return jsonify({"error": "Mensaje vacío"}), 400

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos un asistente útil."},
                {"role": "user", "content": mensaje}
            ]
        )
        texto = respuesta['choices'][0]['message']['content']
        return jsonify({"respuesta": texto})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
