from flask import Flask
import os
import telebot
import threading
from telebot import types

app = Flask(__name__)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

PRONOS = {
    # AFRIQUE - CAN 2027
    "ouganda": "🇺🇬 *OUGANDA vs BOTSWANA*\n📅 Demain 16h GMT - Qualif CAN\n🔥 Victoire Ouganda @1.55\n✅ BANKER - Ouganda solide à domicile",
    "angola": "🇦🇴 *ANGOLA vs SOUDAN DU SUD*\n📅 Demain 19h GMT\n🔥 Victoire Angola @1.35\n✅ GROS BANKER 90%",
    "algerie": "🇩🇿 *ALGERIE vs TOGO*\n📅 Demain 19h GMT\n🔥 Victoire Algérie @1.30\n✅ BANKER DU JOUR 92% - Les Fennecs à la maison",
    
    # EUROPE - Ligue des Nations
    "portugal": "🇵🇹 *PORTUGAL vs DANEMARK*\n📅 Demain 19h45 GMT\n🔥 Victoire Portugal @1.70\n⭐ Ronaldo décisif - Confiance 80%",
    "norvege": "🇳🇴 *NORVEGE vs PAYS DE GALLES*\n📅 Demain 19h45 GMT\n🔥 Haaland buteur + Norvège @2.10\n⚽ Haaland en feu !",
    "suede": "🇸🇪 *SUEDE vs BOSNIE*\n📅 Demain 19h45 GMT\n🔥 Victoire Suède @1.85\n✅ Gyokeres buteur probable",

    # ASIE / MONDE
    "iran": "🇮🇷 *IRAN vs PALESTINE*\n📅 Demain 15h GMT - Amical\n🔥 Victoire Iran @1.40\n✅ Iran supérieur",
}

def menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🇺🇬 Ouganda", callback_data="ouganda"),
        types.InlineKeyboardButton("🇦🇴 Angola", callback_data="angola"),
        types.InlineKeyboardButton("🇩🇿 Algérie", callback_data="algerie"),
        types.InlineKeyboardButton("🇵🇹 Portugal", callback_data="portugal"),
        types.InlineKeyboardButton("🇳🇴 Norvège", callback_data="norvege"),
        types.InlineKeyboardButton("🇸🇪 Suède", callback_data="suede"),
        types.InlineKeyboardButton("🇮🇷 Iran", callback_data="iran"),
    )
    return markup

@bot.message_handler(commands=['start','demain','help'])
def start(m):
    txt = "🔥 *RZ PRONOSTIC - DEMAIN 14 NOV* 🔥\n\n"
    txt += "🌍 *TOUS LES MATCHS DU MONDE:*\n\n"
    txt += "🏆 *AFRIQUE - CAN 2027:*\n🇺🇬 Ouganda vs Botswana\n🇦🇴 Angola vs Soudan du Sud\n🇩🇿 Algérie vs Togo\n\n"
    txt += "🇪🇺 *EUROPE - Ligue des Nations:*\n🇵🇹 Portugal vs Danemark\n🇳🇴 Norvège vs Galles\n🇸🇪 Suède vs Bosnie\n\n"
    txt += "👇 *Clique pour ton prono* 👇"
    bot.send_message(m.chat.id, txt, parse_mode='Markdown', reply_markup=menu())

@bot.callback_query_handler(func=lambda call: True)
def cb(call):
    p = PRONOS.get(call.data)
    if p:
        bot.answer_callback_query(call.id, "Prono chargé!")
        bot.send_message(call.message.chat.id, p, parse_mode='Markdown', reply_markup=menu())

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    t = m.text.lower()
    for k,v in PRONOS.items():
        if k in t:
            bot.reply_to(m, v, parse_mode='Markdown', reply_markup=menu())
            return
    bot.reply_to(m, "👇 Choisis un match de demain !", reply_markup=menu())

@app.route('/')
def home():
    return "RZ MONDIAL Live"

def run_bot():
    print("RZ MONDIAL Bot...")
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
