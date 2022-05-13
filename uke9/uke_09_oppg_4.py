in_storage = {  # dict henta fra oppgaveteksten
    "Ancillary Justice": 1_046,  # vi kan bruke _ i tall, den blir ignorert
    "The Use of Weapons": 372,
    "1984": 5_332,
    "The Three-Body Problem": 523,
    "A Fisherman of the Inland Sea": 728,
}

inn = input("Tittel: ")

while inn != "":
    print(f"Vi har {in_storage.get(inn, 0)} av \"{inn}\"")
    print()

    inn = input("Tittel: ")

print("Ha det!")
