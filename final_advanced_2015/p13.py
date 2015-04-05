"""
    this problem is a to infer a general statement
    we can trick it by using a special example as below
"""

import numpy as np

beta = 0.7

M = np.array([[0  , 1, 0 ],
              [0.5, 0, 0],
              [0.5, 0, 1],
])


def compute_r(S, beta, M):
    
    A = np.zeros(M.shape)
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i in S:
                A[i, j] = beta * M[i, j] + (1 - beta) / len(S)
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
    return r


S1 = set([0, 1]) # teleport set
r1 = compute_r(S1, beta, M)

S2 = set([1]) # teleport set
r2 = compute_r(S2, beta, M)

S3 = set([0]) # teleport set
r3 = compute_r(S3, beta, M)

print
print
print 'r1 : ', r1
print
print 'r2 : ', r2
print
print 'r3 : ', r3
print 

print 'r2-r1 : ', r2 - r1
print '2r1-r2 : ', 2 * r1 - r2
print 'r1-2*r2 : ', r1 - 2 * r2
print 'r1-r2 : ', r1 - r2

# answer is B : 2r1-r2  = r3