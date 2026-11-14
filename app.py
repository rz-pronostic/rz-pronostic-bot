import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

PRONOS = {
    "suede": "🇸🇪 SUÈDE\nHelsingborg vs Orgryte -> 1X & -3.5 buts\nCôte: 1.85 - Confiance 85%",
    "portugal": "🇵🇹 PORTUGAL\nVarzim vs Fafe -> Victoire Varzim\nCôte: 1.95 - Confiance 90%",
    "algerie": "🇩🇿 ALGÉRIE\nMC Alger vs CR Belouizdad -> Les deux marquent\nCôte: 1.80",
    "jour": "🔥 PRONO DU JOUR RZ PRONO\n\n✅ Cumul Côte 4.50\n1. Suède: 1X\n2. Portugal: Varzim Gagne\n3. Algérie: BTTS Oui\n\nBonne chance 🙏"
}

def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🇸🇪 Suède", callback_data="suede"),
        InlineKeyboardButton("🇵🇹 Portugal", callback_data="portugal"),
        InlineKeyboardButton("🇩🇿 Algérie", callback_data="algerie"),
        InlineKeyboardButton("🔥 PRONO DU JOUR", callback_data="jour"),
        InlineKeyboardButton("📊 Stats", callback_data="stats")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Bienvenue chez *RZ PRONOSTIC* 🇧🇫\n\nLe meilleur prono gratuit !\nChoisis ci-dessous 👇", reply_markup=main_menu(), parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "stats":
        text = "📊 *STATS RZ PRONO*\n\n✅ Hier: 2/3 gagnés\n✅ Semaine: 11/15\n✅ Réussite: 78%"
    else:
        text = PRONOS.get(call.data, "Non trouvé")
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=main_menu(), parse_mode='Markdown')

print("Bot RZ Prono V2 lancé...")
bot.infinity_polling()
