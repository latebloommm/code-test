from src.add import add


def test_add():
    assert add(3, 5) == 8


def test_add_negative():
    assert add(-3, 5) == 2


def test_add_zero():
    assert add(10, 0) == 10
