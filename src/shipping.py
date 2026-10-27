def calculate_shipping(weight: float, express: bool = False) -> float:
    """
    Calculate shipping cost.

    Rules:
    - Weight must be greater than zero.
    - Standard shipping costs $4.00 plus $1.25 per pound.
    - Express shipping costs $8.00 plus $2.00 per pound.
    - Return the result rounded to two decimal places.
    """
    raise NotImplementedError