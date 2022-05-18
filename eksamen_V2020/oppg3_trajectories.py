# Eksamen V2020, oppg 15

import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 20

def program_main():
    ts = np.linspace(0, 5, 101)

    for deg in [30, 45, 60]:
        xs = calc_x(ts, deg)
        ys = calc_y(ts, deg)

        plt.scatter(xs[ys > 0], ys[ys > 0],
                    label=f"{deg}$^\circ$")

    plt.legend(loc="upper right")
    plt.title(f"Trajectories. v0 = {v0} m/s")
    plt.xlabel("distance / m")
    plt.ylabel("height / m")

    plt.savefig("trajectory.png")
    plt.show()

def calc_x(time_sequence, angle):
    xs = v0 * time_sequence * np.cos(np.deg2rad(angle))
    return xs

def calc_y(time_sequence, angle):
    ys = v0 * time_sequence * np.sin(np.deg2rad(angle)) - 1/2 * g * np.power(time_sequence, 2)
    return ys



program_main()