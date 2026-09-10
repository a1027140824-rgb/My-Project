"""Simple price and billing utilities."""


def final_price(price: float, discount_percent: float) -> float:
    """Calculate the final price after a discount.

    Args:
        price: Original price. Must be zero or greater.
        discount_percent: Discount from 0 through 100.

    Returns:
        The discounted price rounded to two decimal places.

    Raises:
        ValueError: If price or discount_percent is outside its valid range.
    """
    result = price * (1 - discount_percent / 100)
    return round(result, 2)


def split_bill(total: float, people: int) -> float:
    """Split a bill equally.

    Args:
        total: Total bill amount. Must be zero or greater.
        people: Number of people. Must be greater than zero.

    Returns:
        The amount each person pays, rounded to two decimal places.

    Raises:
        ValueError: If total is negative or people is not positive.
    """
    return round(total / people, 2)


def calculate_tax(price: float, tax_percent: float) -> float:
    """Calculate the tax charged on a price.

    Both arguments must be zero or greater.

    Raises:
        ValueError: If either argument is negative.
    """
    return round(price * tax_percent / 100, 2)


def most_expensive(prices: list[float]) -> float | None:
    """Return the most expensive price, or None for an empty list."""
    if not prices:
        return None

    highest = prices[0]
    for price in prices[1:]:
        if price > highest:
            highest = price

    return highest
