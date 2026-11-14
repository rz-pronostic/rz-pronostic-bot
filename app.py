import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# --- PRONOS (tu peux modifier ici) ---
PRONOS = {
    "suede": "🇸🇪 SUÈDE - Superettan\n\nHelsingborg vs Orgryte -> 1X & -3.5 buts\nCôte: 1.85\nConfiance: 85%",
    "portugal": "🇵🇹 PORTUGAL - Liga 3\n\nVarzim vs Fafe -> Victoire Varzim\nCôte: 1.95\nConfiance: 90%",
    "algerie": "🇩🇿 ALGÉRIE - Ligue 1\n\nMC Alger vs CR Belouizdad -> Les deux marquent\nCôte: 1.80\nConfiance: 80%",
    "jour": "🔥 PRONO DU JOUR - RZ PRONOSTIC\n\n✅ Cumul 3 matchs - Côte totale 4.50\n\n1. Suède: Helsingborg 1X\n2. Portugal: Varzim Gagne\n3. Algérie: BTTS Oui\n\nBonne chance à tous ! 🙏"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇸🇪 Suède", callback_data='suede'), InlineKeyboardButton("🇵🇹 Portugal", callback_data='portugal')],
        [InlineKeyboardButton("🇩🇿 Algérie", callback_data='algerie')],
        [InlineKeyboardButton("🔥 PRONO DU JOUR", callback_data='jour')],
        [InlineKeyboardButton("📊 Mes Stats", callback_data='stats')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Bienvenue chez **RZ PRONOSTIC** !\n\nLe meilleur du prono gratuit au Burkina 🇧🇫\n\nChoisis ton pays ci-dessous 👇",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'stats':
        text = "📊 **STATS RZ PRONO**\n\n✅ Hier: 2/3 gagnés\n✅ Cette semaine: 11/15\n✅ Taux de réussite: 78%\n\nMerci pour votre confiance !"
    else:
        text = PRONOS.get(data, "Prono non trouvé")

    keyboard = [[InlineKeyboardButton("⬅️ Retour au menu", callback_data='menu')]]
    if data != 'menu':
        # pour le bouton retour on renvoie au start
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    else:
        await start_button_menu(query)

async def start_button_menu(query):
    keyboard = [
        [InlineKeyboardButton("🇸🇪 Suède", callback_data='suede'), InlineKeyboardButton("🇵🇹 Portugal", callback_data='portugal')],
        [InlineKeyboardButton("🇩🇿 Algérie", callback_data='algerie')],
        [InlineKeyboardButton("🔥 PRONO DU JOUR", callback_data='jour')],
        [InlineKeyboardButton("📊 Mes Stats", callback_data='stats')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "👋 Bienvenue chez **RZ PRONOSTIC** !\n\nChoisis ton pays ci-dessous 👇",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot RZ Prono V2 lancé...")
    app.run_polling()

if __name__ == '__main__':
    main()
