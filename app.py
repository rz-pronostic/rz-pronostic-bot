import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "RZ PRONOSTIC BOT LIVE - Va sur Telegram /start"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bienvenue sur RZ PRONOSTIC\n\nCommandes:\n/prono - Prono du jour\n/pronos - Tous les pronos\n/stats - Stats")

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 PRONO DU JOUR:\n\n⚽️ PSG vs Marseille: Victoire PSG @1.85\n💰 Mise: 2% bankroll")

async def pronos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 TOUS LES PRONOS:\n1. PSG @1.85\n2. Real @1.70\n3. City Over 2.5 @1.60")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 STATS: 67% Win - +12.5U profit sur 30j ✅")

def run_bot():
    print("Lancement du bot Telegram...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prono", prono))
    app.add_handler(CommandHandler("pronos", pronos))
    app.add_handler(CommandHandler("stats", stats))
    print("Bot en polling...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    print(f"Flask sur port {port}")
    app_flask.run(host='0.0.0.0', port=port)import os
import asyncio
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "RZ PRONOSTIC BOT LIVE 🔥 - /start sur Telegram"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bienvenue sur RZ PRONOSTIC\n\nCommandes:\n/prono - Prono du jour\n/pronos - Tous les pronos\n/stats - Stats")

async def prono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 PRONO DU JOUR:\n\n⚽️ PSG vs Marseille: Victoire PSG @1.85\n💰 Mise: 2% bankroll\n\nAnalyse: PSG en forme à domicile.")

async def pronos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 TOUS LES PRONOS:\n\n1. PSG @1.85 ✅\n2. Real Madrid @1.70 ✅\n3. Over 2.5 Man City @1.60")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 STATS RZ:\n67% Win Rate sur 30j ✅\n+12.5U profit")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

async def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN manquant!")
        return
    print("Bot lance...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("prono", prono))
    application.add_handler(CommandHandler("pronos", pronos))
    application.add_handler(CommandHandler("stats", stats))
    await application.initialize()
    await application.start()
    await application.updater.start_polling(drop_pending_updates=True)
    print("Bot polling started!")
    await application.updater.idle()

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
