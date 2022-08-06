from core.recommendation import *
from core.nearby import *
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from enum import Enum
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

new_df, similarity = recommender()




class Theme(str, Enum):
    historic = "historic"
    religious = "religious"
    park = "park"
    temple = "temple"

    


@app.get("/maris")
async def maris():
    return "chaina"


@app.get("/retrain")
async def retrain():
    global new_df, similarity
    train()
    new_df, similarity = recommender()
    return "Retrain successfull"


@app.get("/rec/{place}")
async def rec(place):
    return recommend(place, similarity, new_df)

@app.get("/{lat}/{long}")
async def displacement(lat: float, long: float):
    return near_location(lat, long)




@app.get("/{theme}")
async def theme_res(theme: Theme):
    temp = []

    with open("data/places.json",'r') as file:
        json_data = json.load(file)
    for place in json_data['attractions']:

        if theme in place['theme']:
            temp_data = {
                    "name": place['name'],
                    "location": place['location'],
                    "cords":  place['cords'],
                    "theme": place['theme'],
                    "image": place['image'],
                    "des": place['des']                        
                    }
            temp.append(temp_data)



    return temp


