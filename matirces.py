import numpy as np

A = np.array([[1, 2], [1, 2]])
B = np.array([[1, 2], [1, 2]])

result = np.array([[0, 0], [0, 0]])

for i in range(len(A)):
    # print("Cantidad de a", len(A))
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print(result)
