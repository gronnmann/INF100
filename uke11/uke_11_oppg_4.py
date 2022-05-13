import random


def find_pi(N):
    random_points = [(random.random(), random.random()) for x in range(N)]

    outsorted = [x for x in random_points if (x[0] ** 2 + x[1] ** 2) <= 1]

    return 4 * len(outsorted) / N
