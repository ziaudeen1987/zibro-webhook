from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8178521099:AAEAPeR47yRXOuF2CcATeco8euSbIzUwDBY"
CHAT_ID = "800494843"

@app.route('/')
def home():
    return "✅ Zibro Webhook is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        message = data.get("message", "⚠️ Zibro alert received (no message)")
        
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload)
        
        return {"status": "ok"}, 200
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
