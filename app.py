from flask import Flask, request
app = Flask(__name__)
PRONOS = {
 "maroc": "MAROC vs NIGER - Victoire Maroc @1.35 BANKER",
 "egypte": "EGYPTE - Victoire Egypte @1.40 - Salah decisif",
 "allemagne": "ALLEMAGNE - Victoire Allemagne @1.85 Value",
 "senegal": "SENEGAL - Victoire Senegal @1.30",
 "nigeria": "NIGERIA - Victoire Nigeria @1.45",
 "can": "CAN CODE: Maroc 1.35 + Egypte 1.40 + Nigeria 1.45 = COTE 2.75",
 "code": "CODE DU JOUR: Maroc + Egypte + Allemagne COTE 3.52",
 "bonjour": "Salut champion! RZ PRONOSTIC Tape: MAROC EGYPTE ALLEMAGNE CAN CODE"
}
@app.route('/')
def home():
 return "RZ PRONOSTIC BOT LIVE!"
@app.route('/webhook', methods=['GET','POST'])
def webhook():
 if request.method == 'GET':
  return request.args.get('hub.challenge','OK')
 return "ok",200
@app.route('/bot')
def bot_test():
 msg = request.args.get('msg','bonjour').lower()
 for k,v in PRONOS.items():
  if k in msg:
   return v
 return PRONOS["bonjour"]
if __name__ == '__main__':
 app.run()
