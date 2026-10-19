from flask import Flask, redirect, render_template, request, url_for, abort
from src.main_lists import (getDestinationList,getDestination,showActivities)

# Inicializamos la aplicación
app = Flask(__name__)
# app.config["SECRET_KEY"] = "mi_clave_secreta_super_segura"

@app.context_processor
def injectActivities():
    return {"activities": showActivities()}

@app.route("/")
def index():
    return render_template(
        "index.html",
        destinations=getDestinationList()
    )

@app.route("/about-us")
def aboutUs():
    return render_template ("about-us.html")

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@app.route("/destinos/<slug>")
def destinationDetail(slug):
    item = getDestination(slug)
    if item is None:
        abort(404)
        
    return render_template("destinationDetail.html", item=item)

if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5001, debug=True)
    