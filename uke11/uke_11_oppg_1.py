def mean(data):
    return sum(data) / len(data)


def median(data):
    size = len(data)

    data.sort()

    return (data[size // 2] + data[size // 2 - 1]) / 2 if size % 2 == 0 else data[size // 2]


def mode(data):
    num = data[0]
    current_count = 0

    for i in data:
        counted = data.count(i)
        if counted > current_count:
            num = i
            current_count = counted

    return num
