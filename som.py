import numpy as np
W = np.random.rand(2)
x = np.array(list(map(float, input("Enter 2 values: ").split())))
print("Initial weights:", W)
for i in range(5):
W = W + 0.2 * (x - W)
print("Iteration", i+1, "weights:", W)
print("Final weights:", W)
Input: 0.2 0.6
