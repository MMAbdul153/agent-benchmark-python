import pytest

from src.text_utils import (
    classify_transactions,
    divide,
    normalize_username,
)


def test_normalize_username():
    assert normalize_username(" Musa Abdulrafiu ") == "musa_abdulrafiu"


def test_normalize_special_characters():
    assert normalize_username("Musa! CS@Student") == "musa_csstudent"


def test_empty_username_rejected():
    with pytest.raises(ValueError):
        normalize_username("!!!")


def test_divide_normal_values():
    assert divide(10, 2) == 5


def test_classify_transactions():
    values = [-4, 0, 20, 99, 100, 500]
    expected = {
        "negative": 1,
        "zero": 1,
        "small": 2,
        "large": 2,
    }
    assert classify_transactions(values) == expected