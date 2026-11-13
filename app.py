from flask import Flask
import os
import telebot
import threading

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

PRONOS = {
    "maroc": "🇲🇦 MAROC vs NIGER - Victoire MAROC @1.35 BANKER CE SOIR 20h",
    "egypte": "🇪🇬 EGYPTE vs MALAWI - Victoire EGYPTE @1.45 CE SOIR 19h",
    "nigeria": "🇳🇬 NIGERIA vs TANZANIE - Victoire NIGERIA @1.50 AUJOURD'HUI 16h",
    "senegal": "🇸🇳 SENEGAL - Repos aujourd'hui, joue Dimanche vs SOUDAN @1.40",
    "burkina": "🇧🇫 BURKINA FASO - Notre équipe analyse les matchs à venir !",
}

@bot.message_handler(commands=['start', 'help'])
def start(m):
    texte = "🔥 RZ PRONOSTIC - PRONOS DU JOUR 🔥\n\n"
    texte += "Tape un nom pour avoir le prono :\n"
    texte += "🇲🇦 maroc\n🇪🇬 egypte\n🇳🇬 nigeria\n🇸🇳 senegal\n🇧🇫 burkina\n\n"
    texte += "Exemple: envoie 'maroc'"
    bot.reply_to(m, texte)

@bot.message_handler(func=lambda m: True)
def prono(m):
    msg = m.text.lower()
    for k,v in PRONOS.items():
        if k in msg:
            bot.reply_to(m, v)
            return
    bot.reply_to(m, "Envoie: maroc, egypte, nigeria, senegal ou burkina pour avoir le prono du jour !")

@app.route('/')
def home():
    return "RZ Pronostic Bot is Running! Go to t.me/rzprono_bf_bot"

def run_bot():
    print("Bot Telegram demarre...")
    bot.infinity_polling()

# Lancer le bot en arriere plan
threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
