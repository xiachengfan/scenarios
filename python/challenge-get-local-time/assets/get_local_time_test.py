import datetime
import unittest
import sys
import pytz

import requests

sys.path.append("/home/labex/project")


from get_local_time import get_local_time


def get_local_time_mine(city):
    # TODO: complete the function
    url = f"http://worldtimeapi.org/api/timezone/Europe/{city}"
    response = requests.get(url)
    if response.status_code == 404:
        return f"Error: {city} not found"
    data = response.json()
    tz = pytz.timezone(data["timezone"])
    local_time = datetime.datetime.now(tz=tz)
    print(f"The local time in {city} is {local_time.strftime('%I:%M %p')}")
    return f"The local time in {city} is {local_time.strftime('%I:%M %p')}"


class TestGetLocalTime(unittest.TestCase):
    def test_valid_city(self):
        self.assertEqual(get_local_time("Paris"), get_local_time_mine("Paris"))
        self.assertEqual(get_local_time("New_York"), get_local_time_mine("New_York"))
        self.assertEqual(get_local_time("Sydney"), get_local_time_mine("Sydney"))

    def test_invalid_city(self):
        self.assertEqual(get_local_time("Fake_City"), get_local_time_mine("Fake_City"))


if __name__ == "__main__":
    unittest.main()
