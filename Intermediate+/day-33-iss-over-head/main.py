import time
import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
user = "simeonpythontest@gmail.com"
password = "wyeszztxzxlndvjq"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data1 = response.json()

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude or MY_LAT+5 <= iss_latitude and iss_longitude <= MY_LONG-5 or iss_longitude<= MY_LONG:
        return True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    tn=time_now.hour
    if tn >= sunset or tn <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(
                from_addr=user,
                to_addrs=user,
                msg="Subject: ISS PROJECT\n\n LOOK UP !!!"
            )


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



