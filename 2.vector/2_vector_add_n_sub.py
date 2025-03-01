"""
    Penjumlahan dan pengurangan vektor hanya bisa dilakukan jika dimensi sama
    Contoh:
        (2,3)+(4,5)=(6,8)
        Tapi (2,3) + (4,5,6) tidak bisa karena dimensinya beda.

    R = ruang dimensi (R, himpunan bilangan real)   
    
    R2= dimensi 2 → Vektor dalam bidang kartesian 2D
        v = (x,y)
    
    R3 = dimensi 3 → Vektor dalam ruang 3D
        v = (x,y,z)
    
    Grafik 2D dan 3D dalam Python
        2D → Bisa digambar dengan matplotlib.pyplot
        3D → Gunakan mpl_toolkits.mplot3d
   
"""

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