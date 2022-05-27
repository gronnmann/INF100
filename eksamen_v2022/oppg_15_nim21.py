import random


def game_loop():
    pinner = 21

    is_player_turn = random.choice([True, False])

    while True:
        print(get_pinner_str(pinner))

        curr_operation = player_turn if is_player_turn else computer_turn

        move = curr_operation(pinner)

        pinner -= move

        if pinner == 0:
            if is_player_turn:
                return False
            else:
                return True

        is_player_turn = not is_player_turn


def computer_turn(pinner: int):
    move = 0
    for i in range(1, 4):
        if pinner-i in [1, 5, 9, 13, 17]:
            move = i

    if move == 0:
        while True:
            move = random.randint(1, 3)

            if valid_move(pinner, move):
                break

    print(f"I take {move} sticks.")
    return move


def player_turn(pinner: int):
    while True:
        player_input = input("Take 1-3 sticks: ")

        try:
            player_move = int(player_input)

            if valid_move(pinner, player_move):
                return player_move
            else:
                print("Sorry, try again!")
        except ValueError:
            print("Sorry, try again!")


def valid_move(pinner: int, move: int):
    if move < 1 or move > 3:
        return False

    if move > pinner:
        return False

    return True


def get_pinner_str(pinner: int):
    return pinner * "/" + (21 - pinner) * "."


if __name__ == "__main__":
    player_score, computer_score = 0, 0
    print("Let's play Nim21")
    while True:
        print(f"The score is me={computer_score} you={player_score}")
        play_input = input("Do you want to play? [y/n] ")
        if play_input == "y":
            if game_loop():
                player_score += 1
            else:
                computer_score += 1
        elif play_input == "n":
            break
        else:
            continue

    print("Thanks for playing!")
