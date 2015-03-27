import numpy as np

beta = 0.8

M = np.array([[1./3, 0, 0],
              [1./3, 0, 0],
              [1./3, 1, 0],

])


S = set([0, 1]) # teleport set

A = np.zeros(M.shape)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if i in S:
            A[i, j] = beta * M[i, j] + (1 - beta) / len(S)
        else:
            A[i, j] = beta * M[i, j]  
print A

print 
print 'answer is A'