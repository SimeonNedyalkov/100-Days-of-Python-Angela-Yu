import requests
from datetime import datetime


APP_ID = "5b53147e"
APP_KEY = "3e023a90c8c28c204a7b196222e45b09"
REMOTE_USER_ID = "e3a70f4f-5124-4617-99b0-83d0c614776b"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/0370be6102c15815935b3ce0982bdd0b/копие наMyWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

ask = input("Tell me which exercises you did? ")

data_json = {
    "query": ask,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 28
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

response = requests.post(url=EXERCISE_ENDPOINT, json=data_json, headers=headers)
result = response.json()
print(result)
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)


