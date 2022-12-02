import requests
from pprint import pprint
SHEETY = "https://api.sheety.co/0370be6102c15815935b3ce0982bdd0b/копие наFlightDeals/prices"
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY)
        response1 = response.json()
        self.destination_data = response1["prices"]
        return self.destination_data


    def get_row_id(self):
        for city in self.destination_data:
            json = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY}/{city['id']}", json=json)
            print(response.text)

