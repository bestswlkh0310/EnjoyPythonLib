import matplotlib.pyplot as plt

def draw_fractal(x1, y1, x2, y2, depth):
    if depth == 0:
        plt.plot([x1, x2], [y1, y2], color='k')
    else:
        x3 = (x1 + x2) / 2 + (y2 - y1) / 2
        y3 = (y1 + y2) / 2 - (x2 - x1) / 2
        draw_fractal(x1, y1, x3, y3, depth - 1)
        draw_fractal(x3, y3, x2, y2, depth - 1)

x1, y1 = -1, 0
x2, y2 = 1, 0

draw_fractal(x1, y1, x2, y2, depth=5)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fractal')

plt.show()