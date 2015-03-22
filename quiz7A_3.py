import numpy as np
from math import sqrt

# example in slide week7_hubs_and_authorities.pdf page 14
"""
A = np.array([[1,1,1],
              [1,0,1],
              [0,1,0],
              ])

n = A.shape[0]

h = np.ones([n,1]) / sqrt(n)
a = np.ones([n,1]) / sqrt(n)

t = 0
print 't = ', t
print h
print
print a
    
while t < 20:
    t += 1
    print '\n\nt =', t
    
    h = np.dot( np.dot(A, A.T), h)
    h = h/ np.linalg.norm(h)
    
    a = np.dot( np.dot(A.T, A), a)
    a = a/ np.linalg.norm(a)
    
    print h
    print
    print a
"""


L = np.array([[0,1,1,0],
              [1,0,0,0],
              [0,0,0,1],
              [0,0,1,0]])

n = L.shape[0]

h = np.ones([n,1])
a = np.dot(L.T, h)

t = 0
while t < 2:
    t += 1
    a = np.dot(L.T, h)
    a = a / max(a)
    h = np.dot(L, a)
    h = h / max(h)
    
    print '\n\nt =', t    
    print h
    print a