# Eksamen V2020, oppg 14
import random

alternatives = {
    0: "Paper",
    1: "Scissors",
    2: "Rock",
}

def test_all_scenarioes():
    for i in range(0, 3):
        for j in range(0, 3):
            winner = find_winner(i, j)

            winner_txt = "Player" if winner == 0 else "Computer"
            if winner == -1:
                winner_txt = "Tie"

            print(f"""
            ====
            Player play: {alternatives[i]}
            Computer play: {alternatives[j]}
            Winner: {winner_txt}
            """)


def start_game():
    round_number = 1
    player_score = 0
    computer_score = 0

    while True:
        print(f"Let's play round {round_number}")

        player_input = input("Your choice (Rock/Paper/Scissors)? ")
        if player_input not in alternatives.values():
            print(f"I don't understand {player_input}. Try again")
            continue

        player_play = {
            "Paper": 0,
            "Scissors": 1,
            "Rock": 2,
        }[player_input]

        computer_play = random.randint(0, 2)

        print(f"Your choice was {alternatives[player_play]}")

        winner = find_winner(player_play, computer_play)

        win_string = "Tie."

        if winner == 0:
            win_string = "You win."
            player_score += 1
        elif winner == 1:
            win_string = "I win."
            computer_score += 1

        print(f"My choice was {alternatives[computer_play]}. {win_string}")

        continue_prompt = input("Continue (y/n)")
        if continue_prompt == "y":
            round_number += 1
            continue
        else:
            break


# Find winner
# returns -1 if tie, 0 if player wins, 1 if computer wins
def find_winner(player_play, computer_play):
    if player_play == computer_play:
        return -1

    if (player_play == 0 and computer_play == 2) or (player_play == 2 and computer_play == 0):
        if player_play == 0 and computer_play == 2:
            return 0
        else:
            return 1

    return 0 if player_play > computer_play else 1


start_game()
