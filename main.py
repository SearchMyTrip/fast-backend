from core.recommendation import *

from fastapi import FastAPI

app = FastAPI()


new_df, similarity = recommender()


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

