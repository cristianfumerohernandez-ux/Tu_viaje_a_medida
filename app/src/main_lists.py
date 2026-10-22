from data.accommodations import accommodations
from data.activities import activities
from data.destinations import destinations


def showActivities():
    destinationNames = {d["slug"]: d["name"] for d in destinations}
    return [
        {
            "name": activity["name"],
            "destination": destinationNames.get(
                activity["destination_slug"], "Destino desconocido"
            ),
        }
        for activity in activities
    ]
    
def getDestinationList():
    result = []
    for d in destinations:
        result.append({
            "slug": d["slug"],
            "name": d["name"],
            "country": d["country"],
            "image": d["image"]
        })
    return result

def getAccomodationsList():
    result = []
    for a in accommodations:
        result.append({
            "slug": a["slug"],
            "name": a["name"],
            "type": a["type"],
            "image": a["image"]
        })
    return result
    
def getAccommodations(slug):
    return next((a for a in accommodations if a["slug"] == slug), None)

# Para las fichas individuales (los enlaces apuntan aquí)
def getDestination(slug):
    return next((d for d in destinations if d["slug"] == slug), None)

def filterDestinations(environment="", no_visa=False):
    return [
        d for d in destinations
        if (not environment or d["environment"] == environment)
        and (not no_visa or not d["is_visa_required"])
    ]

def filterAccommodations(max_price=None, acc_type="", breakfast=False, pets=False):
    result = [
        a for a in accommodations
        if (max_price is None or a["price_per_night"] <= max_price)
        and (not acc_type or a["type"].lower() == acc_type)
        and (not breakfast or a["includes_breakfast"])
        and (not pets or a["allows_pets"])
    ]
    return sorted(result, key=lambda a: a["price_per_night"])