
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite el acceso desde tu página web

# Clave de OpenAI (reemplazala si es necesario)
openai.api_key = "sk-proj-CZbqYA"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message", "")
    
    if not prompt:
        return jsonify({"error": "Mensaje vacío"}), 400

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        mensaje = respuesta.choices[0].message.content
        return jsonify({"reply": mensaje})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
