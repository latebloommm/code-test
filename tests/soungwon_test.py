from src.soungwon import calculate_sum

def test_calculate_sum():
    assert calculate_sum(10) == 55
    assert calculate_sum(5) == 15
    assert calculate_sum(1) == 1
