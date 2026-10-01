"""
Mapa Interactivo - versión Flask
--------------------------------
Python lee datos.json y arma la página completa en el servidor (con
Jinja2). El navegador nunca hace fetch ni maneja JSON directamente:
cada click en un lugar del menú es un link a otra URL, y Flask le
devuelve el HTML ya armado con la info correspondiente.

Requiere: pip install flask
Correr con: python app.py   (y entrar a http://localhost:5000)
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


def cargar_datos():
    with open("datos.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


@app.route("/")
def index():
    lugares = cargar_datos()
    return render_template("mapa.html", lugares=lugares, seleccionado=lugares[0])

@app.route("/lugar/<int:lugar_id>")
def ver_lugar(lugar_id):
    lugares = cargar_datos()

    seleccionado = None  # seleccionado = next((l for l in lugares if l["id"] == lugar_id), None)
    for l in lugares:
        if l["id"] == lugar_id:
            seleccionado = l
            break

    return render_template("mapa.html", lugares=lugares, seleccionado=seleccionado)

if __name__ == "__main__":
    app.run(debug=True)