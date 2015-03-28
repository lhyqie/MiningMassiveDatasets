import numpy as np
from math import sqrt

L = np.array([[0,1,0,0],
              [0,0,1,0],
              [0,0,0,1],
              [0,0,0,0]])

n = L.shape[0]

h = np.ones([n,1])
a = np.dot(L.T, h)

t = 0
while t < 5:
    t += 1
    a = np.dot(L.T, h)
    a = a / max(a)
    h = np.dot(L, a)
    h = h / max(h)
    
    print '\n\nt =', t    
    print h
    print a

# answer is A  (which is FALSE)