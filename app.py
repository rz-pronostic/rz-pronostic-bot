import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "RZ Pronostic Bot is Live!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

PRONOS = {
 "ouganda": "Ouganda - A venir",
 "angola": "Angola vs Soudan du Sud\nVictoire Angola @1.35\nBANKER 90%",
 "algerie": "Algerie - BTTS @1.80",
 "portugal": "Portugal - Varzim @1.95",
 "norvege": "Norvege - A venir",
 "suede": "Suede - 1X & -3.5 buts @1.85",
 "iran": "Iran - A venir"
}

def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Ouganda", callback_data='ouganda'), InlineKeyboardButton("Angola", callback_data='angola')],
        [InlineKeyboardButton("Algerie", callback_data='algerie'), InlineKeyboardButton("Portugal", callback_data='portugal')],
        [InlineKeyboardButton("Norvege", callback_data='norvege'), InlineKeyboardButton("Suede", callback_data='suede')],
        [InlineKeyboardButton("Iran", callback_data='iran')]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue RZ PRONOSTIC BF - Choisis ton pays:", reply_markup=menu())

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(text=PRONOS.get(q.data, "A venir"), reply_markup=menu())

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == '__main__':
    main()
