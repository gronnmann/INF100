import matplotlib.pyplot as plt
from math import sin, pi

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

plt.annotate("Første interseksjonen",
             xy=(pi, 0),
             xycoords="data",
             xytext=(3, 2),
             arrowprops=dict(
                 facecolor = "black",
                 shrink=0.05,
             ))

# savefig lagrer filene
plt.savefig("uke_12_oppg_3.png")

# interaktivt vindu
plt.show()