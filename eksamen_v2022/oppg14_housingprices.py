import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Deloppgave 1
from matplotlib import rcParams

boligprisar = pd.read_csv("housingPriceOsloDecember2018.csv",
                          delimiter=";",
                          encoding="UTF-8",
                          header=0)


def deloppgave_2():
    avg_rom = boligprisar["roomNumber"].mean()

    print(f"Gjennomsnittleg antall rom i Oslo: {avg_rom}")


def deloppgave_3():
    price_decoded = boligprisar["askingPrice(million)"] * 1000000
    price_per_sqm = price_decoded / boligprisar["squareMeter"]

    close = np.isclose(price_per_sqm, boligprisar["kr/sqm"], atol=1)

    print(f"Deloppgave 3: er differansen fra datasettet innan 1? {'Ja' if all(close) else 'Nei'}")


def deloppgave_4(show=True):
    plt.scatter(
        x=boligprisar["floor"],
        y=boligprisar["kr/sqm"],
    )
    plt.title("Kvadratmeterpris per etasje")
    plt.xlabel("Etasje")
    plt.ylabel("Kvadratmeterpris (kr/kvm^2)")

    # Pandas løsning - av en anna grunn breaka den resten av programmet
    # group_by_etasje.plot(
    #     x="floor",
    #     y="kr/sqm",
    #     kind="scatter",
    #     title="Kvadratmeterpris per etasje",
    #     xlabel="Etasje",
    #     ylabel="Kvadratmeterpris (kr/kvm^2)",
    # )

    if show:
        plt.show()


def deloppgave_5(show=True):
    filtered = boligprisar[boligprisar["roomNumber"].isin(range(1, 6))]  # ikkje nødvendig i akkuratt dette
    # datasettet, men greitt å ha om vi skal bruke andre

    find_num = filtered.groupby("roomNumber")["roomNumber"].count()

    plot = find_num.plot(
        kind="bar",
        title="Antall leiligheter med x rom",
        xlabel="Antall rom",
        ylabel="Antall leiligheter"
    )

    if show:
        plt.show()


def deloppgave_6(show=True):
    filtered = boligprisar[boligprisar["roomNumber"].isin(range(1, 6))]  # ikkje nødvendig i akkuratt dette
    # datasettet, men greitt å ha om vi skal bruke andre

    lite_rom = filtered[filtered["roomNumber"] <= 3]
    mange_rom = filtered[filtered["roomNumber"] > 3]

    x = "squareMeter"
    y = "kr/sqm"

    plt.scatter(x=lite_rom[x],
                y=lite_rom[y],
                c="b",
                label="1-3 rom")

    plt.scatter(x=mange_rom[x],
                y=mange_rom[y],
                c="r",
                label="4-5 rom")

    plt.xlabel("Størrelse (kvm^2)")
    plt.ylabel("Kvadratmeterpris (kr/kvm^2)")
    plt.title("Leiligheter sortert på størrelse og kvadratmeterpris")
    plt.legend(loc="best")

    if show:
        plt.show()


def deloppgave_7():
    fig = plt.figure(figsize=(10, 10))  # Juster størrelse slik at alt er lesbart
    # Stack Overflow, 27.05.2022 - https://stackoverflow.com/questions/14770735/how-do-i-change-the-figure-size-with-subplots

    fig.add_subplot(221)
    deloppgave_4(show=False)

    fig.add_subplot(222)
    deloppgave_5(show=False)

    fig.add_subplot(223)
    deloppgave_6(show=False)

    fig.suptitle("Statistikk - Boligprisar i Oslo, desember 2018", fontsize=20)

    plt.show()


# Fiks skalering Stack Overflow, 27.05.2022 - https://stackoverflow.com/questions/6774086/how-to-adjust-padding-with
# -cutoff-or-overlapping-labels
rcParams.update({'figure.autolayout': True})

deloppgave_2()
deloppgave_3()
deloppgave_4()
deloppgave_5()
deloppgave_6()
deloppgave_7()
