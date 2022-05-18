# Eksamen V2021 - Oppgave 16
import random

words = [
    "potetpannekake",
    "oppvaskmaskin",
    "datamaskin",
    "bonanza",
    "joggetur",
    "antibac"
]


def game_loop():
    current_word = words[random.randint(0, len(words) - 1)]
    discovered_chars = []

    for i in range(0, 6):

        print(f"Ordet er {censored_string(current_word, discovered_chars)}")

        user_input = input(f"Bokstav eller løsning ({i + 1}/6): ")

        if user_input == current_word:
            print("Riktig!")
            return

        if len(user_input) > 1:
            continue

        discovered_chars.append(user_input)

    print("Du tapte! Lykke til igjen.")


def censored_string(current_word: str, discovered_chars: list):
    new_word = ["*" if x not in discovered_chars else x for x in current_word]
    return "".join(new_word)


while True:
    game_loop()

    continue_input = input("Vil du fortsette spelet? y/n ")
    if continue_input == "y":
        continue
    else:
        print("Ha det!")
        break
