import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

PRONOS = {
    "suede": "🇸🇪 SUÈDE\nHelsingborg vs Orgryte -> 1X & -3.5 buts\nCôte: 1.85 - Confiance 85%",
    "portugal": "🇵🇹 PORTUGAL\nVarzim vs Fafe -> Victoire Varzim\nCôte: 1.95 - Confiance 90%",
    "algerie": "🇩🇿 ALGÉRIE\nMC Alger vs CR Belouizdad -> Les deux marquent\nCôte: 1.80",
    "jour": "🔥 PRONO DU JOUR RZ PRONO\n\n✅ Cumul Côte 4.50\n1. Suède: 1X\n2. Portugal: Varzim Gagne\n3. Algérie: BTTS Oui\n\nBonne chance 🙏"
}

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🇸🇪 Suède", callback_data='suede'), InlineKeyboardButton("🇵🇹 Portugal", callback_data='portugal')],
        [InlineKeyboardButton("🇩🇿 Algérie", callback_data='algerie')],
        [InlineKeyboardButton("🔥 PRONO DU JOUR", callback_data='jour')],
        [InlineKeyboardButton("📊 Stats", callback_data='stats')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bienvenue chez *RZ PRONOSTIC* 🇧🇫\nLe meilleur prono gratuit !\nChoisis ci-dessous 👇", reply_markup=main_menu(), parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'stats':
        text = "📊 *STATS RZ PRONO*\n\n✅ Hier: 2/3 gagnés\n✅ Semaine: 11/15\n✅ Réussite: 78%"
    else:
        text = PRONOS.get(query.data, "Non trouvé")
    await query.edit_message_text(text=text, reply_markup=main_menu(), parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot RZ V2 lancé...")
    app.run_polling()

if __name__ == '__main__':
    main()
