from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    html = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>RZ BOT</title><style>body{background:#0f0f0f;color:#fff;font-family:Arial;padding:15px}h1{color:#00ff88;text-align:center}.card{background:#1e1e1e;border-left:4px solid #00ff88;padding:15px;margin:12px 0;border-radius:8px}.team{font-weight:bold}.prono{color:#00ff88}</style></head><body><h1>🔥 RZ PRONOSTIC BOT LIVE!</h1><p style="text-align:center">Bot Actif 24/7</p><div class="card"><div class="team">🇲🇦 MAROC vs MOZAMBIQUE</div><div class="prono">✅ Victoire MAROC @1.35 BANKER</div></div><div class="card"><div class="team">🇪🇬 EGYPTE vs NIGERIA</div><div class="prono">✅ Egypte ou Nul</div></div><div class="card"><div class="team">🇸🇳 SENEGAL vs KENYA</div><div class="prono">✅ Victoire SENEGAL @1.30</div></div><div class="card"><div class="team">🇳🇬 NIGERIA vs BENIN</div><div class="prono">✅ Victoire NIGERIA @1.45</div></div><p style="text-align:center;opacity:0.5">v10.4 - LIVE</p></body></html>"""
    return html

PRONOS = {"maroc": "🇲🇦 MAROC vs NIGER - Victoire Maroc @1.35 BANKER","egypte": "🇪🇬 EGYPTE - Victoire Egypte @1.40 - Salah decisif","allemagne": "🇩🇪 ALLEMAGNE - Victoire Allemagne @1.85 Value","senegal": "🇸🇳 SENEGAL - Victoire Senegal @1.30","nigeria": "🇳🇬 NIGERIA - Victoire Nigeria @1.45","can": "🏆 CAN CODE: Maroc 1.35 + Egypte 1.40 + Nigeria 1.45 = COTE 2.75","code": "🎯 CODE DU JOUR: Maroc + Egypte + Allemagne COTE 3.52","bonjour": "Salut champion! RZ PRONOSTIC Tape: MAROC EGYPTE ALLEMAGNE CAN CODE"}

@app.route('/bot')
def bot():
    msg = request.args.get('msg','').lower()
    for k,v in PRONOS.items():
        if k in msg: return v
    return "Salut! Tape: maroc, egypte, senegal, nigeria, allemagne, can, code"

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge','OK')
    return 'OK'

if __name__ == '__main__':
    app.run()
