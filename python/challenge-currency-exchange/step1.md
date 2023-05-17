# Get Exchange Rate

## Introduction

Your task is to create a function in `get_exchange_rate.py` that retrieves the exchange rate between two currencies. The function should take two arguments: the original currency code and the target currency code. The function should use the given json file to get the exchange rate between the two currencies.

## Requirements

1. The function should be named `get_exchange_rate`.
2. The function should take two arguments: `original_currency` (string) and `target_currency` (string).
3. The function should return the exchange rate as a float.
4. If the original currency code or the target currency code is invalid, the function should raise a `ValueError` exception with an appropriate error message.

## Examples

```python
>>> get_exchange_rate("eur", "gbp")
0.885
>>> get_exchange_rate("eur", "cny")
7.614
>>> get_exchange_rate("ABC", "eur")
ValueError: Original currency code not supported
>>> get_exchange_rate("eur", "XYZ")
ValueError: Target currency code not supported
```

The json file returns exchange rates in relation to the USD, so the function first retrieves the exchange rates from the json file and then calculates the exchange rate between the original and target currencies based on the USD exchange rates. If either the original or target currency is invalid, the function raises a ValueError.

1. The `json.load()` function is used to read from a json file.
2. The exchange rate between two currencies is the exchange rate of `target_rate` divide the exchange rate of `original_rate`.
