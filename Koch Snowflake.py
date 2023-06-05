import numpy as np
import matplotlib.pyplot as plt

def koch_snowflake(ax, x, y, length, angle, depth):
    if depth == 0:
        ax.plot(x, y, 'k')
    else:
        x1 = x + length * np.cos(angle)
        y1 = y + length * np.sin(angle)
        x2 = x1 + length * np.cos(angle + np.pi / 3)
        y2 = y1 + length * np.sin(angle + np.pi / 3)
        x3 = x2 + length * np.cos(angle - np.pi / 3)
        y3 = y2 + length * np.sin(angle - np.pi / 3)

        koch_snowflake(ax, x, y, length / 3, angle, depth - 1)
        koch_snowflake(ax, x1, y1, length / 3, angle + np.pi / 3, depth - 1)
        koch_snowflake(ax, x2, y2, length / 3, angle - np.pi / 3, depth - 1)
        koch_snowflake(ax, x3, y3, length / 3, angle, depth - 1)

def plot_koch_snowflake(length, depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    x = [-length/2, length/2, length/2 * np.cos(np.pi / 3), -length/2, -length/2 * np.cos(np.pi / 3)]
    y = [0, 0, length/2 * np.sin(np.pi / 3), 0, -length/2 * np.sin(np.pi / 3)]

    koch_snowflake(ax, x, y, length, 0, depth)

    plt.title('Koch Snowflake')
    plt.show()

# 코확나무 그리기
length = 1
depth = 5

plot_koch_snowflake(length, depth)
