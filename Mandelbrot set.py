import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter

def plot_mandelbrot(x_min, x_max, y_min, y_max, width, height, max_iter):
    image = np.zeros((height, width))

    for i, real in enumerate(np.linspace(x_min, x_max, width)):
        for j, imag in enumerate(np.linspace(y_min, y_max, height)):
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[j, i] = color

    plt.imshow(image, cmap='hot', extent=(x_min, x_max, y_min, y_max))
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.colorbar()
    plt.show()

width = 800
height = 600
max_iter = 1000

plot_mandelbrot(-2.5, 1, -1.5, 1.5, width, height, max_iter)
