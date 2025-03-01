"""
    Temukan solusi sistem persamaan berikut
    
    x + 3y = 12
    2x - 3y = 10
    
    untuk menyelesaikannya dengan program kita
    dapat menggunakan numpy
"""

import numpy as np
import matplotlib.pyplot as plt 
    
def solve_equation(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    hasil = np.linalg.solve(A, B)
    return hasil
    
def grafik(A: np.ndarray, B: np.ndarray) -> None:
    x = np.linspace(-10, 10, 400)
    
    # Koefisien persamaan: Ax + By = C
    a1, b1 = A[0]  # persamaan pertama
    a2, b2 = A[1]  # persamaan kedua
    c1, c2 = B 

    # y dalam bentuk eksplisit: y = (C - Ax) / B
    y1 = (c1 - a1 * x) / b1
    y2 = (c2 - a2 * x) / b2

    # Plot garis
    plt.plot(x, y1, 'b', label=f'{a1}x + {b1}y = {c1}')
    plt.plot(x, y2, 'r', label=f'{a2}x + {b2}y = {c2}')

    plt.legend()
    plt.axhline(0, color='black', linewidth=1)  # Sumbu X
    plt.axvline(0, color='black', linewidth=1)  # Sumbu Y
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.show()
    
def display(A: np.ndarray, B: np.ndarray, desc: str) -> None:
    hasil = solve_equation(A, B)
    print(f"{desc}")
    print(f"Nilai x: {hasil[0]}")
    print(f"Nilai y: {hasil[1]}")
    grafik(A, B)
       
""" 
    x + 3 = 12
    2x - 3y = 10
"""
display(np.array([[1, 3], [2, -3]]), np.array([12, 10]), "Sistem: x + 3y = 12\n\t\t2x - 3y = 10")

""" 
    y = x + 3
    2x - 3y = 10
"""
display(np.array([[-1, 1], [2, -3]]), np.array([3, 10]), "Sistem: y = x + 3\n\t\t2x - 3y = 10")

""" 
    x + 3y = 12
    2x - y = 5
"""
display(np.array([[1, 3], [2, -1]]), np.array([12, 5]), "Sistem: x + 3y = 12\n\t\t2x - 1 = 5")