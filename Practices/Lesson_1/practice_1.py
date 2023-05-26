import numpy as np

# Лінійні операції з векторами
a = [3, 5, 6, 4]
b = [2, 5, 7, 7]

a = np.array(a)
b = np.array(b)

с = a + b
d = a - b
e = a * b
f = a / b
g = np.dot(a, b)  # Скалярний добуток
