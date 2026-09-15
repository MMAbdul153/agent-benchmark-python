def add(a: float, b: float) -> float:
    return a + b

def apply_discount(price: float, discount_percent: float) -> float:
    """
    Apply a percentage discount and round to 2 decimal places.
    Bug: incorrectly handles negative prices and discounts over 100%.
    """
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, 2)

def average(numbers: list[float]) -> float:
    """
    Return the average of a non-empty list.
    Bug: returns 0 for empty list instead of raising ValueError.
    """
    if not numbers:
        return 0.0  # Bug: should raise error
    return sum(numbers) / len(numbers)