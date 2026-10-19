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
