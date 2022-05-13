import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12)

N_steps = 1000000
expected_R = np.sqrt(N_steps)
repeats = 5

max_val = 0
min_val = 0

for i in range(repeats):
    ###################################
    #     generate one random walk    #
    ###################################
    # a list of 4 directions 0,1,2,3
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps, 2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0, 1]  # 0 - right
    steps[dirs == 1] = [0, -1]  # 1 - left
    steps[dirs == 2] = [1, 0]  # 2 - up
    steps[dirs == 3] = [-1, 0]  # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    print("Final position:", steps[-1])


    ###################################
    xs = steps[::, 0]
    ys = steps[::, 1]

    ds = np.sqrt(np.power(xs, 2) + np.power(ys, 2))

    d = np.max(ds)
    # print(f"maxX : {np.max(xs)}, maxY: {np.max(ys)}, dist: {round(d, 1)}")


    max_x = np.max(xs)
    if max_x > max_val:
        max_val = max_x

    max_y = np.max(ys)
    if max_y > max_val:
        max_val = max_y

    min_x = np.min(xs)
    if min_x < min_val:
        min_val = min_x

    min_y = np.min(ys)
    if min_y < min_val:
        min_val = min_y

    # draw only a selection of points, max 5000, to save memory
    skip = N_steps // 5000 + 1
    xs = xs[::skip]
    ys = ys[::skip]

    plt.plot(xs, ys, label=f"maxdist = {round(d, 1)}")

###################################
# add a circle with expected distance
circle = plt.Circle((0, 0), radius=expected_R, color="k")
plt.gcf().gca().add_artist(circle)
# equal axis size
plt.gcf().gca().set_aspect("equal")
###################################

plt.title(f"{repeats} random walks of {N_steps} steps")

bounds = max([max_val, min_val*-1])

plt.xlim([bounds*-1, bounds])
plt.ylim([bounds*-1, bounds])

plt.legend(loc="upper left")

plt.savefig("uke_13_oppg_8.png")
plt.show()
