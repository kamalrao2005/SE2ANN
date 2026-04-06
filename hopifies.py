import numpy as np
p1 = np.array([1, -1, 1, -1])
p2 = np.array([-1, 1, -1, 1])
W = np.outer(p1, p1) + np.outer(p2, p2)
np.fill_diagonal(W, 0)
x = np.array(list(map(int, input("Enter 4 values: ").split())))
print("Initial pattern:", x)
for i in range(5):
x = np.sign(W @ x)
print("Iteration", i+1, ":", x)
print("Final recalled pattern:", x)
Input: 1 -1 1 -1
