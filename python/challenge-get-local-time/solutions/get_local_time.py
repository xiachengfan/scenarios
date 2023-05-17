import requests
import datetime
import pytz


def get_local_time(city):
    url = f"http://worldtimeapi.org/api/timezone/Europe/{city}"
    response = requests.get(url)
    if response.status_code == 404:
        return f"Error: {city} not found"
    data = response.json()
    tz = pytz.timezone(data["timezone"])
    local_time = datetime.datetime.now(tz=tz)
    return f"The local time in {city} is {local_time.strftime('%I:%M %p')}"
