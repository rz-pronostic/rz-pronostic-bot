from flask import Flask
import threading
import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot RZ Pronostic en ligne!"
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)
threading.Thread(target=run_flask, daemon=True).start()

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🔥 *Bienvenue sur RZ PRONOSTIC* 🔥\n\n"
        "Commandes:\n"
        "/prono - Prono du jour\n"
        "/vip - Pronos VIP\n"
        "/stats - Stats"
    )
    await update.message.reply_text(msg, parse_mode='Markdown')

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "⚽ *PRONO DU JOUR - RZ* ⚽\n\n"
        "🏆 Match: Real Madrid vs Barcelona\n"
        "💡 Prono: Double Chance 1X @1.45\n"
        "🔒 Securite: 85%\n\n"
        "Tu veux le VIP ? Tape /vip"
    )
    await update.message.reply_text(msg, parse_mode='Markdown')

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔒 VIP bientôt dispo ! Reste branché.")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Stats RZ: 78% de reussite ce mois ✅")

def main():
    print("Bot lance...")
    if not TOKEN:
        print("BOT_TOKEN manquant")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prono", prono))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("stats", stats))
    app.run_polling()

if __name__ == "__main__":
    main()
