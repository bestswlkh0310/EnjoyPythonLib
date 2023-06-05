import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

plt.show()