import numpy as np
n = int(input("Enter size of square matrix: "))
matrix = []
for i in range(n):
row = list(map(float, input().split()))
matrix.append(row)
matrix = np.array(matrix)
values, vectors = np.linalg.eig(matrix)
print("Eigen values:", values)
print("Eigen vectors:")
print(vectors)
Input:
2
2 0
0 3
