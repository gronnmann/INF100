import csv

artar = {}

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")

    next(akvareader, None)
    next(akvareader, None) # skipper dei to første radene da det berre er headers

    for row in akvareader:
        artar.setdefault(row[12], 0)
        artar[row[12]] += 1


for art, nummer in sorted(artar.items()):
    print(f"{art}: {nummer}")