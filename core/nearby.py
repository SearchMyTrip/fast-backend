import json

from math import sin, cos, sqrt, atan2, radians


def distance(lat1, lon1, lat2, lon2):# approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance 

def near_location(lat, long):
    with open("data/places.json", "r") as file:
        json_data = json.load(file)

    temp = []

    for place in json_data["attractions"]:

        dist = distance(lat,long , place["cords"][0], place["cords"][1])

        temp_data = {
            "name": place["name"],
            "location": place["location"],
            "cords": place["cords"],
            "theme": place["theme"],
            "image": place["image"],
            "des": place["des"],
            "displacement": dist
        }
        temp.append(temp_data)
        temp = sorted(temp, key=lambda x: x['displacement'] )

    return temp


if __name__ == "__main__":
    near_location(26.6524,86.6913)
