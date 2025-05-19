import os

from flask import Flask, send_file

app = Flask(__name__)

post= [
    {"titolo": "Notizia dalla rete: Un nuovo Brawler è in arrivo?" },
    {"titolo": "Aggiornamento Bilanciamento Brawler: Chi sale e chi scende?"},
    {"titolo": "Nuova Skin Leggendaria per Leon Disponibile Ora!"},
]

@app.route("/")
@app.route("/registrazione", methods=["GET"])
def registrazione():
    return send_file('src/registrazione.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    return send_file('src/index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
