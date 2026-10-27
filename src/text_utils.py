import re


def normalize_username(name: str) -> str:
    """
    Convert a display name into a normalized username.

    Rules:
    - Remove leading and trailing whitespace.
    - Convert letters to lowercase.
    - Replace internal whitespace with underscores.
    - Remove characters other than letters, numbers, and underscores.
    - Raise ValueError if the result is empty.
    """
    raise NotImplementedError


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a / b


def classify_transactions(amounts: list[float]) -> dict[str, int]:
    result = {"negative": 0, "zero": 0, "small": 0, "large": 0}

    for amount in amounts:
        if amount < 0:
            result["negative"] += 1
        else:
            if amount == 0:
                result["zero"] += 1
            else:
                if amount < 100:
                    result["small"] += 1
                else:
                    result["large"] += 1

    return result