from scipy.sparse import coo_matrix
import numpy as np

col = [0,0,1,2]
row = [1,2,2,2]
value = [1./2,1./2,1.,1.]

n = 3
beta = 0.7 

M = coo_matrix((value, (row,col)), shape=(n, n))
print M
print M.shape
print

A =  beta * M + (1-beta)/n * np.ones([n,n])
print A
print A.shape
print


r = np.ones([n,1])
print r
print 

for i in range(10):
    r =  A * r
    print i
    print r
    print r.sum()
    print 