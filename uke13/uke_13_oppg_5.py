import numpy as np


def polynomial(a: float, b: float, c: float, d: float, xs: np.ndarray):
    ys = a * np.power(xs, 3) + b * np.power(xs, 2) + c * xs + d

    return ys


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    xs = np.linspace(-6, 6)

    ys = polynomial(-1, -1.5, 8, 25, xs)

    plt.plot(xs, ys)
    plt.grid(alpha=0.5, linestyle="--")

    # Adds axis to the plot
    ax = plt.gca()
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    plt.show()