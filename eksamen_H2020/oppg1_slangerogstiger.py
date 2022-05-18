# Eksamen H2020 - oppg 13

import random


def roll_dice():
    return random.randint(1, 6)


snarvegar = {
    3: 8,
    9: 13,
    10: 2,
    15: 6,
}

player_num = 100000
num_fields = 15


def simulate(rounds):
    player_data = [0] * player_num
    player_rounds = [0] * player_num

    i = 0
    for round_num in range(0, rounds):
        for player_index, player_felt in enumerate(player_data):
            rolled = roll_dice()

            nytt_felt = player_felt + rolled
            if nytt_felt > num_fields:
                nytt_felt = nytt_felt - (num_fields + 1)
                player_rounds[player_index] += 1

            nytt_felt = snarvegar.get(nytt_felt, nytt_felt)

            player_data[player_index] = nytt_felt

    for x in range(0, 16):
        print(f"{round((player_data.count(x) / player_num) * 100)}", end=" ")
    print()

    for x in range(0, num_fields + 1):
        how_many = player_rounds.count(x)
        print(f"{how_many} players managed {x} rounds ({round((how_many / player_num) * 100)}%)")


simulate(20)
