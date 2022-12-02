import requests
from data_manager import DataManager
import json
kiwi = "https://tequila-api.kiwi.com/"
dm = DataManager()
from datetime import datetime

import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    def get_destination_code(self, city_name):
        now = datetime.now().strftime("%d/%m/%Y")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        parameters = {
            "fly_from": "VAR",
            "fly_to": city_name,
            "dateFrom": now,
            "dateTo": now
        }
        response = requests.get(url=location_endpoint, headers=headers, params=parameters)
        results = response.json()
        code = results
        return code