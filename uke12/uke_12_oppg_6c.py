import csv

lats = []
lons = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2]) # latitude is second last
            lon = float(row[-1]) # longitude is last
        except ValueError:
            continue

        vann_int = 1 if row[20] == "SALTVANN" else 0

        lats.append((lat, vann_int))
        lons.append((lon, vann_int))


try:
    import matplotlib.pyplot as plt

    plt.plot([x[0] for x in lons if x[1] == 1], [x[0] for x in lats if x[1] == 1], "+b")
    plt.plot([x[0] for x in lons if x[1] == 0], [x[0] for x in lats if x[1] == 0], "+c")

    plt.savefig("uke_12_oppg_6c.png")

    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
