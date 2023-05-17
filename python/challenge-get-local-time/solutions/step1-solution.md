# Solution

The `get_local_time` function uses the `requests` library to connect to the API `http://worldtimeapi.org/api/timezone/Europe/{city}` and retrieve the timezone information for the specified city.

Then, after get the data (json), we use `pytz` library to get the timezone of the city.

The function then uses the `datetime` library to calculate the local time in the given city by the timezone. The function returns a string representing the local time in the given city in a readable format.
