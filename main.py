import resultado as fundamentus
import yahoofinance as yah
import detalhes
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Acesso restrito"

@app.route("/<key>/<papeis>")
def hello_world(key, papeis):
    if(key == "gab2020"):        
        return jsonify(yah.get_cotacao(papeis))
    else:
        return "Não autorizado"
    
@app.route("/<key>/papel/<papel>")
def get_detalhes_papel(key, papel):
    if(key == "gab2020"):
        return jsonify(yah.get_detalhes_papel(papel))        
    else:
        return "Não autorizado"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
