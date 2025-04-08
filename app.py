from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

message = {
    "text": "Willkommen!",
    "timestamp": datetime.now(timezone.utc).isoformat()
}

@app.route("/")
def home():
    return "ESP32-Nachrichtenserver läuft!"

@app.route("/send", methods=["POST"])
def send():
    global message
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Kein Text übergeben"}), 400
    message = {
        "text": data["text"],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    return jsonify({"status": "Nachricht gespeichert"})

@app.route("/get", methods=["GET"])
def get():
    return jsonify(message)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gibt hier den Port vor
    app.run(host="0.0.0.0", port=port)
