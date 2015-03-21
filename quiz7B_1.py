import numpy as np

beta = 0.7

M = np.array([[0  , 1, 0, 0],
              [0.5, 0, 0, 0],
              [0.5, 0, 0, 1],
              [0  , 0, 1, 0],
])


S = set([0]) # teleport set

A = np.zeros(M.shape)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if i == 0:  # Assume that pages selected for the teleport set are nodes 1 and 2 and that in the teleport set, 
                            # the weight assigned for node 1 is twice that of node 2
            A[i, j] = beta * M[i, j] + 2./ 3 * (1 - beta) / len(S)
        elif i == 1:
            A[i, j] = beta * M[i, j] + 1./ 3 * (1 - beta) / len(S)
        else:
            A[i, j] = beta * M[i, j]  
print A

n = M.shape[0]
r = np.ones([n,1])
r = r / n

print r

t = 0
while t < 100:
    t += 1
    print 't =', t
    r = np.dot(A, r) 
    print r
    
    