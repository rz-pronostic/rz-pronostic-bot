from flask import Flask
import threading
import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

# --- PARTIE FLASK POUR RENDER (obligatoire) ---
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot RZ Pronostic en ligne!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask, daemon=True).start()

# --- PARTIE BOT TELEGRAM ---
TOKEN = "MET TON TOKEN ICI"  # <-- Remets ton token BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot RZ Pronostic en ligne ! Tape /prono")

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pronostic du jour : Victoire Algérie 1.182 ✅")

def main():
    print("Bot lancé...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prono", prono))
    app.run_polling()

if __name__ == "__main__":
    main()
