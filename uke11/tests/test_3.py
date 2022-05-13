import random
from itertools import count, compress

try:
    import uke_11_oppg_3 as D
except ModuleNotFoundError:
    import oppgaver.uke_11_oppg_3 as D


def generator(n):
    pass_fail_col = [random.randint(0, 1) for _ in range(n)]
    iterator = count(start=1, step=1)
    id_list = list(next(iterator) for _ in range(n))
    return id_list, pass_fail_col


def zipped_sln(col1, col2):
    zipped = list(zip(col1, col2))
    result = []
    for student, score in zipped:
        if score == 1:
            result.append(student)
    return result


def test_example():
    id_col = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    pass_fail_col = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    assert D.select_pass(id_col, pass_fail_col) == [5, 6, 8, 12, 15]


def test_100():
    id_list = generator(100)[0]
    pass_fail_col = generator(100)[1]

    assert D.select_pass(id_list, pass_fail_col) == zipped_sln(id_list, pass_fail_col)


def test_200():
    id_list = generator(200)[0]
    pass_fail_col = generator(200)[1]

    assert D.select_pass(id_list, pass_fail_col) == zipped_sln(id_list, pass_fail_col)
