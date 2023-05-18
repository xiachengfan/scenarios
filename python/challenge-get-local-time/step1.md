# Get Local Time

Your program should connect to the API `http://worldtimeapi.org/api/timezone/Europe/{city}`, retrieve the timezone information for the specified city, and calculate the local time in the specified city. The output should look something like :

```python
"The local time in {city} is XX:XX AM/PM" # XX:XX is the local time in Paris, AM/PM needs to be specified
```

## Input

- `city` - A string representing the name of a city in the world.

## Output

- A string representing the local time in the given city in a readable format.

## Example

```python
# Input:
city = "Paris"
# Output:
"The local time in Paris is XX:XX AM/PM" # XX:XX is the local time in Paris, AM/PM needs to be specified
```

```python
# Input:
city = "New York"
# Output:
"The local time in New York is XX:XX AM/PM" # XX:XX is the local time in New York, AM/PM needs to be specified
```

## Note

- Your program must take as input the name of a city in the world.
- Your program must connect to an API to retrieve timezone information. You can use `requests` to connect to the API and the `pytz` library to convert tha data to the timezone
- Your program must use the timezone information to calculate the local time in the given city. You can use `datetime` to calculate the local time.
- Your program must output the local time in the given city in a readable format.
