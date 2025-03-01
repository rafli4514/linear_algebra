"""
   Symbols dalam Aljabar Linear  
    -Matrix: A, M, C  
    -Vector: v, u, w  
    -Scalar: a (alpha), B (beta), λ (lambda)  

   Definisi:
    
    1. Matriks adalah kumpulan angka yang tersusun dalambaris dan kolom.  
       Bisa dianggap sebagai kumpulanvektor baris atauvektor kolom.  

       Contoh matriks 2x3:
       A = | 1  2  3 |
           | 4  5  6 |

    2. Vektor adalah objek matematis yang memilikibesar dan arah.  
       Bisa direpresentasikan sebagaivektor baris atauvektor kolom.  

       Contoh vektor di R²:
       v = | 2 |
           | 3 |

    3. Skalar adalah bilangan riil yang digunakan untuk mengalikan vektor atau matriks.  
       Skalar bisa mengubah panjang (besar) vektor, tetapi tidak mengubah arah (kecuali dikalikan dengan negatif).  

       Contoh skalar λ:
       Jika λ = 2 dan v = (2,3), maka:
       λ * v = (4,6)
       
    
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1: int = np.array([-3, 4])
scalar: int = -3

v: int = scalar * v1

plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot([0, v[0]], [0, v[1]], 'r', label='v')

plt.legend()
plt.axis('square')
axlim = max([abs(max(v1)), abs(max(v))*1.5])
plt.axis((-axlim, axlim, -axlim, axlim))
plt.grid()
plt.show()

