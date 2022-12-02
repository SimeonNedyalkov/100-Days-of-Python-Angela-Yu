import requests
from twilio.rest import Client
account_sid = 'AC7c444605ac8430800b6d25ab3bc6e339'
auth_token = "fd937233eb14eee4e4d60027a3cf4663"
api_key = "bf9fc2a2d7a673acdf6e50e2f223e4c2"
omw_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
        'lon': 27.914734,
        'lat': 43.214050,
        'appid': api_key,
        'exclude': 'current,minutely,daily',
}




response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]


def its_raining():
    for item in range(0, 12):
        weather_id = hourly_data[item]["weather"][0]["id"]
        if weather_id < 700:
            return True

if its_raining() == True:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= "Днес ще вали!☂️",
        from_= "+12532432332",
        to='+359893444257'
    )

    print(message.status)
