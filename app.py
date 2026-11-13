from flask import Flask, request

app = Flask(__name__)

PRONOS = {
    "maroc": "🇲🇦 MAROC vs NIGER\n✅ Victoire Maroc @1.35 BANKER FORT\nMaroc invincible à domicile - CAN + Mondial",
    "egypte": "🇪🇬 EGYPTE\n✅ Victoire Egypte @1.40\nSalah décisif, à jouer sans peur",
    "allemagne": "🇩🇪 ALLEMAGNE\n✅ Victoire Allemagne @1.85\nValue Bet Mondial",
    "senegal": "🇸🇳 SENEGAL\n✅ Victoire Sénégal @1.30",
    "nigeria": "🇳🇬 NIGERIA\n✅ Victoire Nigeria @1.45",
    "can": "🏆 CAN 2026 - CODE COMPLET:\n🇲🇦 Maroc 1.35\n🇪🇬 Egypte 1.40\n🇳🇬 Nigeria 1.45\nCOTE TOTALE: 2.75\nMise: 10.000F",
    "code": "🎯 CODE DU JOUR RZ PRONOSTIC:\nMaroc + Egypte + Allemagne\nCOTE: 3.52\nInbox pour bookmakers",
    "bonjour": "Salut champion! RZ PRONOSTIC ici 👋\nTape:\nMAROC\nEGYPTE\nALLEMAGNE\nCAN\nCODE",
    "salut": "Salut champion! RZ PRONOSTIC ici 👋\nTape:\nMAROC\nEGYPTE\nALLEMAGNE\nCAN\nCODE"
}

@app.route('/')
def home():
    return "RZ PRONOSTIC BOT LIVE! Tape /bot?msg=maroc pour tester"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge','OK')
    return "ok", 200

@app.route('/bot')
def bot_test():
    msg = request.args.get('msg','bonjour').lower()
    for k,v in PRONOS.items():
        if k in msg:
            return v.replace("\n","<br>")
    return PRONOS["bonjour"].replace("\n","<br>")

if __name__ == '__main__':
    app.run()
