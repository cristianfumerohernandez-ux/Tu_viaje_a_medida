from data.accommodations import accommodations
from data.activities import activities
from data.destinations import destinations


def showActivities():
    destinationNames = {d["slug"]: d["name"] for d in destinations}
    return [
        {
            "slug": activity["slug"],
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
        })
    return result

def getAccomodationsList():
    result = []
    for a in accommodations:
        result.append({
            "slug": a["slug"],
            "name": a["name"],
            "type": a["type"],
        })
    return result
    
def getAccommodations(slug):
    return next((a for a in accommodations if a["slug"] == slug), None)

def getActivities(slug):
    return next((a for a in activities if a["slug"] == slug), None)

# Para las fichas individuales (los enlaces apuntan aquí)
def getDestination(slug):
    return next((d for d in destinations if d["slug"] == slug), None)