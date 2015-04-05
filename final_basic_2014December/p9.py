"""
Suppose the Web consists of four pages A, B, C, and D, that form a chain
A-->B-->C-->D
We wish to compute the PageRank of each of these pages, but since D is a "dead end," we
will "teleport" from D with probability 1 to one of the four pages, each with equal probability. We
do not teleport from pages A, B, or C. Assuming the sum of the PageRanks of the four pages
is 1, what is the PageRank of page B, correct to two decimal places?
"""
import numpy as np

beta = 0.7

A = np.array([[0, 0, 0, 0.25],
              [1, 0, 0, 0.25],
              [0, 1, 0, 0.25],
              [0, 0, 1, 0.25],
])




n = A.shape[0]
r = np.ones([n,1])
r = r / n

print r

t = 0
while t < 100:
    t += 1
    print '\nt =', t
    r = np.dot(A, r) 
    print r
    print 'sum(r)=', r.sum()
    