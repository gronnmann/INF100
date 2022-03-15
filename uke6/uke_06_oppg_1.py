def remove_fives(start_list):

    for i in range(start_list.count(5)):
        start_list.remove(5)

    return start_list


def every_third(start_list):
    return start_list[::3]


def reverse(start_list):
    return start_list[::-1]


def halve_values(start_list):
    return list(map((lambda x: x / 2.0), start_list))


def unique_values(start_list):
    already_unique = []
    new_list = []

    for i in range(len(start_list)):
        val = start_list[i]

        if start_list.count(val) <= 1:  # ikkje vits å sjekke med verdiar det berre finst 1 av
            new_list.append(val)
            continue

        if already_unique.count(val) < 1:
            already_unique.append(val)
            new_list.append(val)

    return new_list


def my_len(obj):
    n = 0
    for i in obj:
        n += 1
    return n
