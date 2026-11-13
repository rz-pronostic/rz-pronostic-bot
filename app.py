from flask import Flask, request, render_template_string
app = Flask(__name__)

PRONOS = {
  "maroc": "🇲🇦 MAROC vs NIGER - Victoire MAROC @1.35 BANKER CE SOIR 20h",
  "egypte": "🇪🇬 EGYPTE vs MALAWI - Victoire EGYPTE @1.45 CE SOIR 19h",
  "nigeria": "🇳🇬 NIGERIA vs TANZANIE - Victoire NIGERIA @1.50 AUJOURD'HUI 16h",
  "senegal": "🇸🇳 SENEGAL - Repos aujourd'hui, joue Dimanche vs SOUDAN @1.40"
}

HTML = """
<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>RZ PRONOSTIC</title>
<style>body{background:#000;color:#fff;font-family:Arial;padding:20px;text-align:center} .card{background:#111;border:2px solid #00ff00;border-radius:15px;padding:15px;margin:10px} h1{color:#00ff00} .btn{background:#00ff00;color:#000;padding:15px 30px;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:10px}</style>
</head><body>
<h1>🔥 RZ PRONOSTIC - PRONOS DU JOUR 🔥</h1>
<p>Matchs du Vendredi 13 Novembre 2026</p>
{% for k,v in pronos.items() %}
<div class="card"><h3>{{ v }}</h3></div>
{% endfor %}
<a class="btn" href="https://t.me/rzpronostic">REJOINDRE TELEGRAM</a>
<p style="margin-top:20px;color:#888">Bot mis à jour à 19:55 - Pronos du jour validés</p>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, pronos=PRONOS)

@app.route('/bot')
def bot():
    msg = request.args.get('msg','').lower()
    for k,v in PRONOS.items():
        if k in msg:
            return v
    return "Envoie: maroc, egypte, nigeria ou senegal pour avoir le prono du jour ! Matchs de ce soir."
    
if __name__ == '__main__':
    app.run()
