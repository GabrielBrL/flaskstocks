import fundamentus
import json
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/<key>")
def hello_world(key):
    if(key == "gab2020"):
        df = fundamentus.get_resultado()
        dictionary = df.to_dict(orient='index')
        json_resultado = json.dumps(dictionary)
        return json_resultado
    else:
        return "Não autorizado"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
