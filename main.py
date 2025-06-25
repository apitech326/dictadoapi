from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"  # Reemplaza con tu clave real
API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/api/correct", methods=["POST"])
def correct():
    user_input = request.json.get("text", "")
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "Corrige la ortografía y gramática del siguiente texto."},
                {"role": "user", "content": user_input}
            ]
        }
    )
    data = response.json()
    corrected = data["choices"][0]["message"]["content"]
    return jsonify({"corrected": corrected})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
