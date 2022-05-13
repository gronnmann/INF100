# test different values for n, k in function
from statistics import StatisticsError, mean, median, mode

try:
    import oppgaver.uke_11_oppg_1 as M
except ModuleNotFoundError:
    import uke_11_oppg_1 as M

TEST_DATA = [
    [3, 1, 7, -3, 5, 9, 1, 5, 9, 7, -3, 7],
    [1, 1, 1],
    [1, 2, 0],
    [1, 2, 7],
    [-1, 1],
    [-1, -9],
    [-100, 100],
    [555, 33, 23, -23, 3333, 4232, -5994],
]


def test_mean():
    for test_case in TEST_DATA:
        assert (
            abs(M.mean(test_case) - mean(test_case)) < 1e-6
        ), f"Your function for calculating the mean seems to be incorrect."


def test_median():
    for test_case in TEST_DATA:
        # assert M.median(test_case) == median(test_case), f"Your function for calculating the median seems to be incorrect."
        assert (
            abs(M.median(test_case) - median(test_case)) < 1e-6
        ), f"Your function for calculating the median seems to be incorrect."


def test_mode():
    for test_case in TEST_DATA:
        try:
            # assert M.mode(test_case) == mode(test_case), f"Your function for calculating the mode seems to be incorrect."
            assert (
                abs(M.mode(test_case) - mode(test_case)) < 1e-6
            ), f"Your function for calculating the mode seems to be incorrect."
        except StatisticsError as e:
            pass
