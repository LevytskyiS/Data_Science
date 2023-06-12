import numpy as np

a = np.array([[1], [2], [3]])
b = np.array([[3], [4], [3]]).T
print(a.shape, b.shape)
c = np.dot(a, b)

print(c)
