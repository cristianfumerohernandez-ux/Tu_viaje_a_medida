from flask import Flask, redirect, render_template, request, url_for, abort

# Inicializamos la aplicación
app = Flask(__name__)
# app.config["SECRET_KEY"] = "mi_clave_secreta_super_segura"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about-us")
def aboutUs():
    return render_template ("about-us.html")

if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5001, debug=True)
    