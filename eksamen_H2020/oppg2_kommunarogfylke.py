import csv

fylker = {} # admin1: (name, befolkning)

kommunar = [] # (name, befolkning, admin1)

def oppg_a():
    with open("NO_ADM12.csv", "r", encoding="UTF-8") as opened_file:
        reader = csv.DictReader(opened_file, delimiter=";")

        for row in reader:

            if row["feature code"] == "ADM1":
                fylker.setdefault(row["admin1 code"], (row["name"], int(row["population"])))

            elif row["feature code"] == "ADM2":
                kommunar.append((row["name"], int(row["population"]), row["admin1 code"]))

def oppg_b():
    sorted_kommuner = sorted(kommunar, key=lambda x: x[1], reverse=True)

    print(f"{sorted_kommuner}")

    minste_fem = sorted_kommuner[-5:]
    storste_fem = sorted_kommuner[:5]

    print("============= Fem største kommunar =============")
    for kommune in storste_fem:
        print(f"{kommune[0]} ({kommune[1]} personar)")
    print("==========================")
    print()
    print("============= Fem minste kommunar =============")
    for kommune in minste_fem:
        print(f"{kommune[0]} ({kommune[1]} personar)")
    print("==========================")

def oppg_c():
    print_fylke("01")

def print_fylke(fylke_num):
    fylke = fylker.get(fylke_num)

    print("==========================")

    print(f"{fylke_num} {fylke[0]}")

    print("==========================")

    kommunar_in_fylke = [x for x in kommunar if x[2] == fylke_num]
    kommunar_in_fylke = sorted(kommunar_in_fylke, key=lambda x: x[0])

    for kommune in kommunar_in_fylke:
        print("{:<16} {:<9}".format(kommune[0], kommune[1]))

def oppg_d():
    while True:
        user_input = input("Search word [q to quit]? ")

        if user_input == "q":
            break


        found = False
        for fylkeid, fylkedata in fylker.items():
            fylkenavn = fylkedata[0]

            if user_input.lower() in fylkenavn.lower():
                print_fylke(fylkeid)
                found = True
                continue

        if not found:
            print("No matching fylke found. Try again.")


oppg_a()
oppg_b()
oppg_c()
oppg_d()
