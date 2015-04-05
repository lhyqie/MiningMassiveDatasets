import numpy as np
from math import sqrt

A = np.array([[0,1,1,1,1],
              [1,0,1,1,1],
              [1,1,0,1,1],
              [1,1,1,0,1],
              [1,1,1,1,0]
              ])

D = np.sum(A,0)
D = np.diag(D)

print A
print
print D
print

L = D - A
print L
print

print np.linalg.norm(L)**2

sum = 0
for i in xrange(L.shape[0]):
    for j in xrange(L.shape[1]):
        sum += L[i,j] ** 2
print 'asnwer is :', sum


# C