import csv

lats = {}
lons = {}

# Viser forskjellige tillatelser basert på formål

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2])  # latitude is second last
            lon = float(row[-1])  # longitude is last
        except ValueError:
            continue

        lats.setdefault(row[10], [])
        lons.setdefault(row[10], [])

        lats[row[10]].append(lat)
        lons[row[10]].append(lon)

try:
    import matplotlib.pyplot as plt

    for formaal, notused in sorted(lats.items(), key=lambda x: len(x[1]), reverse=True): # sorter etter størrelse
        plt.plot(lons[formaal], lats[formaal], "+", label=f"{formaal} (n={len(lons[formaal])})")

    plt.legend(loc="lower right")

    plt.title("Akvakulturtillatelser fra Akvakulturregisteret basert på formål")

    plt.axis("off") # lite grunn til å ha aksane

    plt.savefig("uke_12_oppg_6d.png")

    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} categories loaded')
