import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# dua vector dalam R2(dimensi)
v1 = np.array([3, 4])
v2 = np.array([2, 6])

v = v1 + v2;

# buat grafik
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot([0, v2[0]] + v1[0], [0, v2[1]] + v1[1], 'r', label='v2')
plt.plot([0, v[0]], [0, v[1]], 'k', label='v1 + v2')

plt.legend()
plt.axis('square')
plt.axis((-10, 10, -10, 10))
plt.grid()
plt.show()