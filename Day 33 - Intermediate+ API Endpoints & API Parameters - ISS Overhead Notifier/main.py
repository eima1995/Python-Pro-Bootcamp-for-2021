import requests
from datetime import datetime
from config import MY_LAT,MY_LONG
import time


def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if float(MY_LAT) - 5 <= iss_latitude <= float(MY_LAT) + 5 and\
            float(MY_LONG) - 5 <= iss_latitude <= float(MY_LONG) + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_over_head() and is_night():
        print('Send email')
    else:
        time_to_sleep = 60
        print(f'Waiiting {time_to_sleep} s.')
        time.sleep(time_to_sleep)
