import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "RZ PRONOSTIC BOT LIVE 🔥"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bienvenue sur RZ PRONOSTIC\n\n/prono - Prono du jour\n/pronos - Tous les pronos\n/stats - Stats")

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 PRONO DU JOUR:\nPSG vs Marseille: Victoire PSG @1.85")

async def pronos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 TOUS LES PRONOS:\n1. PSG @1.85\n2. Real @1.70\n3. City Over @1.60")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 STATS: 67% Win - +12.5U ✅")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    print("Lancement bot dans main thread...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prono", prono))
    app.add_handler(CommandHandler("pronos", pronos))
    app.add_handler(CommandHandler("stats", stats))
    print("Bot en polling - nettoyage conflit...")
    # Supprime tout webhook / ancien polling
    import asyncio
    async def clean():
        await app.bot.delete_webhook(drop_pending_updates=True)
    asyncio.get_event_loop().run_until_complete(clean())
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
