import json


def to_json(data):
    with open("data/places.json",'r') as file:
        data = json.load(file)
    print(data['attractions'])
        


if __name__ == "__main__":
    print(
        to_json(
            [
                "Kopan Monastery",
                "Pashupatinath Temple",
                "Namo Buddha (Stupa)",
                "Budhanilkantha",
                "Thamel",
                "Mahendra Cave",
                "Boudhanath Stupa",
                "Kumari Chowk",
                "Shree Bindhyabasini Temple",
                "Devi's Fall",
                "Tal Barahi",
                "Rupa Taal",
                "Swayambhunath Temple",
                "Chandragiri Hills",
                "Garden of Dreams",
                "Kathmandu Durbar Square",
                "Shivapuri Nagarjun National Park",
                "Kailashnath Mahadev",
                "Dakshinkali Temple",
                "Hanuman Dhoka",
                "Narayanhiti Palace Museum",
                "Basantapur Tower",
                "Phewa Lake",
                "Begnas Lake",
                "International Mountain Museum",
                "Chamero Gufa",
            ]
        )
    )
