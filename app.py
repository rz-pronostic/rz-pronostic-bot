from flask import Flask
import threading
import os

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot RZ Pronostic en ligne!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask, daemon=True).start()
