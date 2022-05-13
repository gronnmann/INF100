def collatz_sequence(n):  # kode henta fra oppgaveteksten - https://folk.uib.no/dgr061/INF100/22V/uke_09/index.html
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def first_ten_collatz():
    first_ten = {}

    for i in range(1, 11):
        first_ten[i] = collatz_sequence(i)

    return first_ten
