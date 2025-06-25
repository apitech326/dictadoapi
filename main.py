from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("DEEPSEEK_API_KEY")
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
