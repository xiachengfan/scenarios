# Currency Converter

## Introduction

Your task is to create a function in `currency_conversion.py` that converts an amount of money from one currency to another. The function should take three arguments: the original currency code, the target currency code, and the amount of money to be converted.

## Requirements

1. The function should be named `currency_converter`.
2. The function should take three arguments: `original_currency` (string), `target_currency` (string), and `amount` (float).
3. The function should use the given json file to get the exchange rate between the two currencies.
4. The function should return the converted amount as a float.

## Examples

```python
>>> currency_converter("eur", "gbp", 100)
88.532
>>> currency_converter("eur", "cny", 100)
761.402
>>> currency_converter("ABC", "gbp", 100)
ValueError: Original currency code not supported
>>> currency_converter("gbp", "XYZ", 100)
ValueError: Target currency code not supported
```

1. This function calls the function `get_exchange_rate()` in step 1 which retrieves the exchange rate between the two currencies.
2. The converted amount is the `amount` of money multiplied by `exchange_rate`.
