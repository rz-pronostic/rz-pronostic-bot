import os, threading, requests
from flask import Flask
from datetime import datetime
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)
@app.route('/')
def home(): return "RZ PRONOSTIC LIVE", 200

# VRAIS MATCHS DU 15 NOV 2026
MATCHS_JOUR = [
    {"league":"Nations League C 17h","match":"Chypre vs Montenegro","prono":"Montenegro ou Nul @1.65","analyse":"Chypre très faible à domicile"},
    {"league":"Nations League C 17h","match":"Lettonie vs Armenie","prono":"Under 3.5 buts @1.30 SAFE","analyse":"2 défenses fermées"},
    {"league":"Nations League C 20h","match":"Finlande vs San Marino","prono":"Finlande -2.5 @1.40","analyse":"Finlande doit marquer bcp"},
    {"league":"Nations League C 20h","match":"Belarus vs Albanie","prono":"Albanie gagne @1.85","analyse":"Albanie en forme"},
    {"league":"Nations League A 22h45","match":"Belgique vs Italie","prono":"Over 1.5 @1.26 SAFE","analyse":"Match ouvert"},
    {"league":"Nations League A 22h45","match":"France vs Turquie","prono":"France gagne @1.17 SAFE","analyse":"France à domicile très fort"},
    {"league":"Nations League A 22h45","match":"Espagne vs Angleterre","prono":"Over 1.5 @1.23 SAFE","analyse":"CHOC - 2 attaques feu"},
    {"league":"Nations League A 22h45","match":"Croatie vs Tchequie","prono":"Over 1.5 @1.24","analyse":"Croatie favori"},
]

@bot.message_handler(commands=['start'])
def start(m): bot.reply_to(m, "🔥 RZ PRONOSTIC - MATCHS RÉELS DU JOUR 15/11\n\n/pronos pour voir les 8 vrais matchs\n/prono pour le SAFE")

@bot.message_handler(commands=['prono'])
def prono(m):
    ma = MATCHS_JOUR[5] # France
    bot.reply_to(m, f"🔥 SAFE DU JOUR\n\n🏆 {ma['league']}\n🏟️ {ma['match']}\n💡 Prono: {ma['prono']}\n📝 {ma['analyse']}\n\n💰 Cote: 1.17 - Confiance 84%")

@bot.message_handler(commands=['pronos'])
def pronos(m):
    txt = f"📋 VRAIS MATCHS AUJOURD'HUI 15/11 ({len(MATCHS_JOUR)} matchs)\n\n"
    for i, ma in enumerate(MATCHS_JOUR,1):
        txt+=f"{i}. [{ma['league']}] {ma['match']}\n   👉 {ma['prono']}\n\n"
    txt+="💡 Combi SAFE: France + Finlande + Over Espagne = @2.10"
    bot.reply_to(m, txt)

def run_bot(): bot.infinity_polling()
threading.Thread(target=run_bot, daemon=True).start()
if __name__ == '__main__': app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
