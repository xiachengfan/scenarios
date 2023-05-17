from get_exchange_rate import get_exchange_rate


def currency_conversion(original_currency, target_currency, amount):
    """
    Convert one currency to another based on the exchange rate.

    Args:
    original_currency (str): The three-letter currency code for the original currency.
    target_currency (str): The three-letter currency code for the target currency.
    amount (float): The amount of the original currency to be converted.

    Returns:
    float: The equivalent amount of the target currency.
    """
    # Retrieve exchange rate
    exchange_rate = get_exchange_rate(original_currency, target_currency)

    # Convert currency
    converted_amount = amount * exchange_rate

    return converted_amount
