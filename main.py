import yahoofinance as yah
import selic
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Acesso restrito"
    
@app.route("/<key>/<papel>/<variacao>")
def get_variacao(key,papel,variacao):
    if(key == "gab2020"):
        return jsonify(yah.get_hist(papel,variacao))
    else:
        return "Não autorizado"
    
@app.route("/<key>/papel/<papel>")
def get_detalhes_papel(key, papel):
    if(key == "gab2020"):
        return jsonify(yah.get_detalhes_papel(papel))        
    else:
        return "Não autorizado"

@app.route("/<key>/dividends/<papel>")
def get_divs(key, papel):
    if(key == "gab2020"):
        return jsonify(yah.get_history_dividends(papel))        
    else:
        return "Não autorizado"

@app.route("/<key>/taxa/<papel>")
def get_taxas(key, papel):
    if(key == "gab2020"):
        return jsonify(selic.get_rates(papel))
    else:
        return "Não autorizado"
        
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, port=os.getenv("PORT", default=5000))
