import numpy as np
import matplotlib.pyplot as plt


xmin, xmax = -2., 1.
ymin, ymax = -1.5, 1.5
num_pixels = 1000

# initial setup of calculation constant C for each pixel
X = np.linspace(xmin, xmax, num_pixels)[None,:]
Y = np.linspace(ymin, ymax, num_pixels)[:,None]
C = X + 1j * Y
# start value of Z is always 0
Z = np.zeros_like(C)
# P counts iterations, this is what we plot at the end
P = np.zeros_like(C, dtype='uint8') # unsigned int 0..255

# iteration of Z <- Z*Z + C
for i in range(120):
    # print(f"Iteration {i}")
    # which elements are still "live"?
    live = np.abs(Z) < 2.
    # update live pixels with current iteration number
    P[live] = i 
    # iterate
    Z[live] = Z[live]*Z[live] + C[live] 

plt.imshow(
    P, 
    origin='lower',
    extent=(X.min(), X.max(), Y.min(), Y.max())
)

plt.show()

plt.savefig("mandelbrot.png")
