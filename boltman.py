import numpy as np
W = np.random.rand(2, 2)
x = np.array(list(map(float, input("Enter 2 values: ").split())))
print("Initial input:", x)
for i in range(3):
x = 1 / (1 + np.exp(-W @ x))
print("Step", i+1, "output:", x)
print("Final output probabilities:", x)
Input: 0.5 0.8
