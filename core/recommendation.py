import numpy as np
import pandas as pd
import json
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ps = PorterStemmer()

def train():
    places = pd.read_csv("data/output.csv")
    places["location"] = places["location"].apply(lambda x: x.split())
    places["des"] = places["des"].apply(lambda x: x.split())
    places["location"] = places["location"].apply(lambda x: [i.replace(",", "") for i in x])
    places["location"] = places["location"].apply(lambda x: [i.replace(" ", "") for i in x])
    places["des"] = places["des"].apply(lambda x: [i.replace(",", "") for i in x])
    places["des"] = places["des"].apply(lambda x: [i.replace(" ", "") for i in x])
    places["tags"] = places["location"] + places["des"]
    new_df = places[["name", "cords", "tags"]]
    new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
    
    def stem(text): 
        y = []
        for i in text.split(): 
            y.append(ps.stem(i))
        return " ".join(y)
    new_df['tags'] = new_df['tags'].apply(stem)
   
    cv = CountVectorizer(max_features=3000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()
    cv.get_feature_names()
    
    file = open("core/model/model.pkl", "wb")
    similarity = cosine_similarity(vectors)
    pickle.dump(new_df, file)
    pickle.dump(similarity, file)
    file.close()

def recommender(): 
    file = open("core/model/model.pkl", "rb")
    new_df = pickle.load(file)
    similarity = pickle.load(file)
    file.close()
    return (new_df, similarity)

def recommend(place, similarity, new_df):

    places = pd.read_csv("data/output.csv")

    place_index = new_df[new_df['name']==place].index[0]
    distances = similarity[place_index]
    place_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])
    # names = new_df['name']
    temp = []

    
    with open("data/places.json",'r') as file:
        json_data = json.load(file)
    for i in place_list:
        for place in json_data['attractions']:
            if place['name'] == places['name'][i[0]]:
                temp_data = {
                        "name": place['name'],
                        "location": place['location'],
                        "cords":  place['cords'],
                        "theme": place['theme'],
                        "image": place['image'],
                        "des": place['des']                        
                        }
                temp.append(temp_data)

            



        # print(json_data['attractions'])

        # temp.append(places['name'][i[0]])

    return temp 

if __name__ == "__main__":
    new_df, similarity = recommender() 
    print(recommend('Phewa Lake', similarity, new_df))
