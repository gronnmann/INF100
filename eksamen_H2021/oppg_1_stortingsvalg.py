# Eksamen H2021 - Stortingsvalg
import csv

multiplier = [*range(1, 100, 2)]


def mandatfordeling(filnavn, antall_mandater):
    valgdistrikt = []  # [distriktsnavn, n_mandater, fordelingstall, multiplier, fordelingstall_start]

    with open(filnavn, "r", encoding="UTF-8") as valgdistrikt_file:
        valgdistrikt_reader = csv.reader(valgdistrikt_file, delimiter=",")
        next(valgdistrikt_reader, None)  # skip header

        for distrikt in valgdistrikt_reader:
            valgdistrikt.append([
                distrikt[0],
                0,
                find_fordelingstall(int(distrikt[1]), int(distrikt[2])),
                0,
                find_fordelingstall(int(distrikt[1]), int(distrikt[2])),
            ]
            )

    stemme_data = {}  # distrikt: mandatar

    while sum([x[1] for x in valgdistrikt]) < antall_mandater:
        biggest_distrikt = max(valgdistrikt, key=lambda x: x[2])

        biggest_distrikt[1] += 1
        biggest_distrikt[2] = biggest_distrikt[4] / multiplier[biggest_distrikt[3]]
        biggest_distrikt[3] += 1

        stemme_data.setdefault(biggest_distrikt[0], 0)
        stemme_data[biggest_distrikt[0]] += 1

    return stemme_data


def find_fordelingstall(innbyggere, kvadratkilometer):
    return (innbyggere + kvadratkilometer) * 1.8


fordeling = mandatfordeling("valgdistrikt_2020-01-01.csv", 169)

fordeling = dict(sorted(fordeling.items(), key=lambda x: x[1], reverse=True))

print("{:<20} {:<20}".format("Distrikt", "Mandater"))
print("=" * 22)

for distrikt, mandater in fordeling.items():
    print("{:<20} {:<20}".format(distrikt, mandater))
