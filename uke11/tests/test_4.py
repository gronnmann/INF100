try:
    import uke_11_oppg_4 as D
except ModuleNotFoundError:
    import oppgaver.uke_11_oppg_4 as D


def test_100():
    assert 2.7 <= D.find_pi(100) <= 3.5


def test_1000():
    assert 2.9 <= D.find_pi(1000) <= 3.3


def test_10000():
    assert 3.0 <= D.find_pi(10000) <= 3.2


def test_10000000():
    assert 3.135 <= D.find_pi(10000000) <= 3.149
