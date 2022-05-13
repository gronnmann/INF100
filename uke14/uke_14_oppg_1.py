import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):
    sealevels = pd.read_csv(
        filename,
        delimiter=" ",
        header=None,
        names=["year", "month", "day", "hour", "sealevel"],
    )

    sealevels["hour"] -= 1

    dates = pd.to_datetime(sealevels[["year", "month", "day", "hour"]])

    sealevels.insert(loc=0, column="date", value=dates)

    return sealevels


def plot_months(dataframe: pd.DataFrame):
    monthly_avg = dataframe.groupby("month")["sealevel"].mean().reset_index()

    monthly_avg.plot(x="month", y="sealevel", title="Gjennomsnittleg havnivå for kvar månad", xlabel="Månad",
                     ylabel="Havnivå", label="Havnivå")

    plt.minorticks_on()
    plt.show()


def plot_rolling_average(dataframe: pd.DataFrame):
    juni_data = dataframe[(dataframe["month"] == 6)]

    juni_data["rolling_sealevel"] = juni_data["sealevel"].rolling(24, 1).mean()

    print(juni_data.head())

    juni_data.plot(x="date", y=["sealevel", "rolling_sealevel"],
                   label=["Raw Data", "Rolling average"],
                   color=["cyan", "orange"],
                   title="Havnivå i Juni",
                   xlabel="Dag",
                   ylabel="Havnivå")

    plt.savefig("uke_14_oppg_1.png")
    plt.show()
