from flask import Flask, redirect, render_template, request, url_for, abort
from src.main_lists import (
    getDestinationList,
    getDestination,
    showActivities,
    getAccomodationsList,
    getAccommodations,
    getActivities,
    filterDestinations,
    filterAccommodations,
    filterBySlug
)

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
        destinations=getDestinationList(),
        accommodations=getAccomodationsList(),
    )


@app.route("/about-us")
def aboutUs():
    return render_template("about-us.html")


@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404


@app.route("/destinos/<slug>")
def destinationDetail(slug):
    item = getDestination(slug)
    if item is None:
        abort(404)
    accommodationsFil,activitiesFil = filterBySlug(slug)
    return render_template("destinationDetail.html", item=item,accommodationsFil = accommodationsFil, activitiesFil=activitiesFil)


@app.route("/alojamientos/<slug>")
def accommodationsDetails(slug):
    item = getAccommodations(slug)
    if item is None:
        abort(404)

    destination = getDestination(item["destination_slug"])
    if destination is None:
        abort(404)

    return render_template(
        "accommodationsDetails.html",
        item=item,
        destination=destination,
    )


@app.route("/actividad/<slug>")
def activitiesDetails(slug):
    item = getActivities(slug)
    if item is None:
        abort(404)

    destination = getDestination(item["destination_slug"])
    if destination is None:
        abort(404)

    return render_template(
        "activitiesDetails.html",
        item=item,
        destination=destination,
    )


@app.route("/search")
def searchIndex():
    return redirect(url_for("search", mode="destinos"))


@app.route("/search/<mode>")
def search(mode):
    if mode not in ("destinos", "alojamientos", "medida"):
        abort(404)

    args = request.args
    environment = args.get("environment", "")
    if mode not in ("destinos", "alojamientos", "medida"):
        mode = "destinos"

    environment = args.get("environment", "")
    acc_type = args.get("type", "")
    max_price = args.get("max_price", type=float)  # None si está vacío o no es número
    no_visa = args.get("no_visa") == "on"
    breakfast = args.get("breakfast") == "on"
    pets = args.get("pets") == "on"

    found_destinations, found_accommodations, combos = [], [], []

    if mode == "destinos":
        found_destinations = filterDestinations(environment, no_visa)

    elif mode == "alojamientos":
        found_accommodations = filterAccommodations(
            max_price, acc_type, breakfast, pets
        )

    else:  # "medida": solo destinos con al menos un alojamiento que cumpla todo
        accommodations_ok = filterAccommodations(max_price, acc_type, breakfast)
        for d in filterDestinations(environment, no_visa):
            matches = [
                a for a in accommodations_ok if a["destination_slug"] == d["slug"]
            ]
            if matches:
                combos.append({"destination": d, "accommodations": matches})

    return render_template(
        "search.html",
        mode=mode,
        f=args,
        found_destinations=found_destinations,
        found_accommodations=found_accommodations,
        combos=combos,
        destinations_by_slug={d["slug"]: d for d in filterDestinations()},
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5001, debug=True)
