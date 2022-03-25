def valgresultat(parties, votes, seats):
    votesOriginal = [float(x) for x in votes]
    votes = [float(x) / 1.4 for x in votes]

    multiplier = [1.0] * seats

    counter = list(map(list, zip(parties, votes, multiplier, votesOriginal)))

    seats_array = []

    while seats > 0:
        chosen_seat = max(counter, key=lambda index: index[1])

        print(f"Chose seat: {16 - seats}: {chosen_seat}")

        seats_array.append((chosen_seat[1], chosen_seat[0]))

        chosen_seat[2] = chosen_seat[2] + 2.0

        chosen_seat[1] = chosen_seat[3] / chosen_seat[2]

        seats = seats - 1

    return seats_array


def parti_mandater(party_list, votes, seats):
    mandater = valgresultat(party_list, votes, seats)

    # unzipped = list(zip(*mandater))

    counted = dict()
    stemmetall = []

    for stemme, parti in mandater:
        if parti in counted:
            counted[parti] += 1
        else:
            counted[parti] = 1
            stemmetall.append(int(round(stemme * 1.4, 0)))

    returned_list = []

    for i, parti in enumerate(counted):
        returned_list.append((parti, stemmetall[i], counted[parti]))

    print(f"{returned_list}")

    return returned_list
