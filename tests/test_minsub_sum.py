import pytest
from src.minsub_sum import sum_to_n


def test_sum_to_ten():
    assert sum_to_n(10) == 55


def test_sum_to_one():
    assert sum_to_n(1) == 1


def test_sum_to_zero():
    assert sum_to_n(0) == 0


def test_negative_input():
    with pytest.raises(ValueError):
        sum_to_n(-1)
