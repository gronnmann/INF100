import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("tkagg")


airports = [] # airport format (tuple) - (IATA, size, bredde, lengde)

with open("airport-codes.csv", encoding="UTF-8", mode="r") as airport_file:
    data_reader = csv.DictReader(airport_file, delimiter=",")

    for row in data_reader:

        split_coords = row["coordinates"].split(", ")

        airports.append(
            (
                row["iata_code"], row["type"], float(split_coords[0]), float(split_coords[1])
            )
        )


plt.scatter([x[3] for x in airports], [x[2] for x in airports], s=[1 if x[1] == "medium_airport" else 10 for x in airports], color="orange")

for x in [x for x in airports if x[1] == "large_airport"]:
    plt.annotate(x[0], (x[3], x[2]))


plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Airports")

plt.savefig("uke_14_oppg_2")

plt.show()