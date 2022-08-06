import math
import json
from math import radians, cos, sin, asin, sqrt


def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    return (
        2
        * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
        * 6371
    )


def near_location(lat, long):
    with open("data/places.json", "r") as file:
        json_data = json.load(file)
    temp = []
    for place in json_data["attractions"]:
        
        temp_data = {
            "name": place["name"],
            "location": place["location"],
            "cords": place["cords"],
            "theme": place["theme"],
            "image": place["image"],
            "des": place["des"],
            "displacement": distance(lat, place["cords"][0], long, place["cords"][1]),
        }
        temp.append(temp_data)

    return temp



if __name__ == "__main__":
    print(distance(27.7149, 27.7215, 85.2903, 85.3620))
