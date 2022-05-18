# Eksamen V2021 - Oppg 17
import csv
import matplotlib.pyplot as plt

airports = []  # (iata, big??, lengde, bredde)

with open("airport-codes.csv", "r", encoding="UTF-8") as airports_file:
    airports_as_csv = csv.DictReader(airports_file, delimiter=",")

    for airport in airports_as_csv:
        airports.append(
            (
                airport["iata_code"],
                True if airport["type"] == "large_airport" else False,
                float(airport["coordinates"].split(", ")[1]),
                float(airport["coordinates"].split(", ")[0]),
            )
        )

plt.scatter(
    x=[x[2] for x in airports],
    y=[x[3] for x in airports],
    s=[10 if x[1] else 1 for x in airports]
)

for large_airport in [x for x in airports if x[1]]:
    plt.annotate(large_airport[0], (large_airport[2], large_airport[3]))

plt.title("Flyplassar rundt om i verda")
plt.xlabel("Langdegrader")
plt.ylabel("Breddegrader")


plt.show()
