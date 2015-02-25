import numpy as np
from test.test_normalization import NormalizationTest
U = np.array([
 #M #N #P #Q #R
 [1, 2, 3, 4, 5], #A
 [2, 3, 2, 5, 3], #B
 [5, 5, 5, 3, 2], #C
])

def normalizeRow(U):
    res = np.empty(U.shape)
    for i in xrange(U.shape[0]):
        row_mean = U[i,:].mean()
        #print row_mean
        for j in xrange(U.shape[1]):
            res[i, j] = U[i, j] - row_mean
    return res

def normalizeColumn(U):
    res = np.empty(U.shape)
    for j in xrange(U.shape[1]):
        col_mean = U[:,j].mean()
        #print col_mean
        for i in xrange(U.shape[0]):
            res[i, j] = U[i, j] - col_mean
    return res
    
print U
print 

U1 = normalizeRow(U)
print U1
print


U2 = normalizeColumn(U1)
print U2
print
