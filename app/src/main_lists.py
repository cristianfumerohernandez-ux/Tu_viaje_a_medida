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
        })
    return result

# Para las fichas individuales (los enlaces apuntan aquí)
def getDestination(slug):
    return next((d for d in destinations if d["slug"] == slug), None)