import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# Petit serveur pour que Render dise "Live"
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "RZ Pronostic Bot is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

PRONOS = {
    "ouganda": "🇺🇬 OUGANDA\nÀ venir...",
    "angola": "🇦🇴 ANGOLA vs SOUDAN DU SUD\nDemain 19h GMT\nVictoire Angola @1.35\nGROS BANKER 90% ✅",
    "algerie": "🇩🇿 ALGÉRIE\nMC Alger vs CR Belouizdad -> Les deux marquent @1.80",
    "portugal": "🇵🇹 PORTUGAL\nVarzim vs Fafe -> Victoire Varzim @1.95 - 90%",
    "norvege": "🇳🇴 NORVÈGE\nÀ venir...",
    "suede": "🇸🇪 SUÈDE\nHelsingborg vs Orgryte -> 1X & -3.5 buts @1.85",
    "iran": "🇮🇷 IRAN\nÀ venir..."
}

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🇺🇬 Ouganda", callback_data='ouganda'), InlineKeyboardButton("🇦🇴 Angola", callback_data='angola')],
        [InlineKeyboardButton("🇩🇿 Algérie", callback_data='algerie'), InlineKeyboardButton("🇵🇹 Portugal", callback_data='portugal')],
        [InlineKeyboardButton("🇳🇴 Norvège", callback_data='norvege'), InlineKeyboardButton("🇸🇪 Suède", callback_data='suede')],
        [InlineKeyboardButton("🇮🇷 Iran", callback_data='iran')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bienvenue chez *RZ PRONOSTIC* 🇧🇫\nChoisis ton pays 👇", reply_markup=main_menu(), parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = PRONOS.get(query.data, "Prono à venir...")
    await query.edit_message_text(text=text, reply_markup=main_menu(), parse_mode='Markdown')

def main():
    threading.Thread(target=run_flask).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot RZ Prono lancé...")
    app.run_polling()

if __name__ == '__main__':
    main()
