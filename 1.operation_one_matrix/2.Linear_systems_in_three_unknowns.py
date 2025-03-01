import numpy as np
import matplotlib.pyplot as plt

def solve_equation(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    hasil = np.linalg.solve(A, B)
    return hasil

def grafik(A: np.ndarray, B: np.ndarray) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-10, 10, 30)
    y = np.linspace(-10, 10, 30)
    X, Y = np.meshgrid(x, y)
    
    a1, b1, c1 = A[0]
    a2, b2, c2 = A[1]
    a3, b3, c3 = A[2]
    d1, d2, d3 = B
    
    Z1 = (d1 - a1*X - b1*Y) / c1
    Z2 = (d2 - a2*X - b2*Y) / c2 
    Z3 = (d3 - a3*X - b3*Y) / c3 
     
    ax.plot_surface(X, Y, Z1, alpha=0.5, color='red', label='persamaan 1')
    ax.plot_surface(X, Y, Z2, alpha=0.5, color='blue', label='persamaan 2')
    ax.plot_surface(X, Y, Z3, alpha=0.5, color='green', label='persamaan 3')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()

def display(A: np.ndarray, B: np.ndarray, desc: str) -> None:
    hasil = solve_equation(A, B)
    print(f"{desc}")
    print(f"Nilai x: {hasil[0]}")
    print(f"Nilai y: {hasil[1]}")
    print(f"Nilai z: {hasil[2]}")
    grafik(A, B)


"""
    3a - 3b + 4c = -23
    a + 2b - 3c = 25
    4a - b + 2c = 25
"""
display(np.array([
    [3, -3, 4],
    [1, 2, -3],
    [4, -1, 2]
    ]),
    np.array(
        [-23, 25, 25]
    ),
    "Sistem: 3x - 3y + 4z = -23\n\tx - 2y - 3z = 25\n\t4x - y + 2z = 25"
    )

"""
    -x - 5y + z = 17
    -5x - 5y + 5z = 5
    2x + 5y - 3z = -10
"""
display(np.array([
    [-1, -5, 1],
    [-5, -5, 5],
    [2, 5, -3]
    ]),
    np.array(
        [17, 5, 10]
    ),
    "Sistem: -x - 5y + z = 17\n\t-5x -5y + 5z = 5\n\t2x + 5y - 3z = -10"
    )

