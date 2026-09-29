def add(a: float, b: float) -> float:
    return a + b

def apply_discount(price: float, discount_percent: float) -> float:
    """
    Apply a percentage discount and round to 2 decimal places.
    """
    if price < 0:
        raise ValueError("price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, 2)

def average(numbers: list[float]) -> float:
    """
    Return the average of a non-empty list.
    """
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)
