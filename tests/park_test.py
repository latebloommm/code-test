from src.park_code import lotto
from unittest.mock import patch

def test_lotto_win(capsys):
    with patch("src.park_code.random.randint", return_value=5):
        lotto(5)

    captured = capsys.readouterr()
    assert captured.out.strip() == "당첨"


def test_lotto_fail(capsys):
    with patch("src.park_code.random.randint", return_value=7):
        lotto(5)

    captured = capsys.readouterr()
    assert captured.out.strip() == "꽝 당첨번호는7입니다."
