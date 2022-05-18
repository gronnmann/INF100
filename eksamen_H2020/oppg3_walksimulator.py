import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12)

N_steps = 1000000
expected_R = np.sqrt(N_steps)
repeats = 5

max_away = 0

for x in range(0, repeats):
    ###################################
    #     generate one random walk    #
    ###################################
    # a list of 4 directions 0,1,2,3
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps,2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0,1]  # 0 - right
    steps[dirs == 1] = [0,-1] # 1 - left
    steps[dirs == 2] = [1,0]  # 2 - up
    steps[dirs == 3] = [-1,0] # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    print(f'Final position for walk {x}: {steps[-1]}')

    xs = steps[:, 0]
    ys = steps[:, 1]
    max_x = np.max(xs)
    min_x = np.min(xs)
    max_y = -1 * np.max(ys)
    min_y = -1 * np.min(ys)

    max_away = max_x if max_x > max_away else max_away
    max_away = max_y if max_y > max_away else max_away
    max_away = min_x if min_x > max_away else max_away
    max_away = min_y if min_y > max_away else max_away

    ds = np.sqrt((np.power(xs, 2) + np.power(ys, 2)))
    max_dist = np.max(ds)


    ###################################
    # draw only a selection of points, max 5000, to save memory
    skip = N_steps // 5000 + 1
    xs = xs[::skip]
    ys = ys[::skip]
    plt.plot(xs, ys, label=f"maxdist = {round(max_dist, 1)}")
    ###################################


###################################
# add a circle with expected distance
circle = plt.Circle((0,0), radius=expected_R, color='k')
plt.gcf().gca().add_artist(circle)
# equal axis size
plt.gcf().gca().set_aspect('equal')
###################################

plt.xlim((-max_away, max_away))
plt.ylim((-max_away, max_away))
plt.legend(loc="upper left")

plt.title(f"{repeats} random walks of {N_steps} steps")

plt.show()
