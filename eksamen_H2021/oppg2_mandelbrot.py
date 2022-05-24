import numpy as np
import matplotlib.pyplot as plt


def mandel(x: int, y: int, size: int, pixels: int, filename: str):
    xmin, xmax = x, x+size
    ymin, ymax = y, y+size

    X = np.linspace(xmin, xmax, pixels)[None, :]
    Y = np.linspace(ymin, ymax, pixels)[:, None]
    C = X + 1j * Y
    # start value of Z is always 0
    Z = np.zeros_like(C)
    # P counts iterations, this is what we plot at the end
    P = np.zeros_like(C, dtype='uint8')  # unsigned int 0..255

    # iteration of Z <- Z*Z + C
    for i in range(120):
        # print(f"Iteration {i}")
        # which elements are still "live"?
        live = np.abs(Z) < 2.
        # update live pixels with current iteration number
        P[live] = i
        # iterate
        Z[live] = Z[live] * Z[live] + C[live]

    plt.imshow(
        P,
        origin='lower',
        extent=(X.min(), X.max(), Y.min(), Y.max())
    )


    plt.savefig(filename)

def mandel_zoom(old_x: int, new_x: int, old_y : int, new_y : int, old_size: int, new_size: int, pixels : int, num_steps: int):
    X_linear = np.linspace(start=old_x,
                           stop=new_x,
                           num=num_steps)
    Y_linear = np.linspace(start=old_y,
                           stop=new_y,
                           num=num_steps)

    size_linear = np.linspace(start=old_size,
                              stop=new_size,
                              num=num_steps)

    for i in range(len(X_linear)):
        mandel(x=X_linear[i],
               y=Y_linear[i],
               size=size_linear[i],
               pixels=pixels,
               filename=f"zoom_{i+1:02}.png")


def validate_number(input_str: str):
    try:
        temp = int(input_str)
        return True
    except ValueError:
        return False


def program_main():
    num_pixels, num_images = 0, 0

    while True:
        pixels_str = input("Pixels: ")
        if validate_number(pixels_str):
            num_pixels = int(pixels_str)
            break

    while True:
        images_str = input("Num images: ")
        if validate_number(images_str):
            num_images = int(images_str)
            break

    mandel_zoom(-2, -0.725, -1.5, 0.335, 3, 0.02, num_pixels,
                num_images)



program_main()