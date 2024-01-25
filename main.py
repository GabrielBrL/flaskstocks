import fundamentus
import json
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "acesso restrito"

@app.route("/<key>")
def hello_world(key):
    if(key == "gab2020"):
        df = fundamentus.get_resultado()    
        dictionary = df.to_dict(orient='index')
        json_resultado = jsonify(dictionary)
        return json_resultado
    else:
        return "Não autorizado"
    
@app.route("/<key>/<papel>")
def get_detalhes(key, papel):
    if(key == "gab2020"):
        df = fundamentus.get_detalhes_papel(papel)
        dictionary = df.to_dict(orient='index')
        json_resultado = jsonify(dictionary)
        return json_resultado
    else:
        return "Não autorizado"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
