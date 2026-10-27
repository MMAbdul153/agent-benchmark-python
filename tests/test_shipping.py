import pytest

from src.shipping import calculate_shipping


def test_standard_shipping():
    assert calculate_shipping(4) == 9.00


def test_express_shipping():
    assert calculate_shipping(4, express=True) == 16.00


def test_zero_weight_rejected():
    with pytest.raises(ValueError):
        calculate_shipping(0)