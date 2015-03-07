import numpy as np
A = np.array(
    [
        #A B C D E F G H
        [0,0,1,0,0,1,0,0],
        [0,0,0,0,1,0,0,1],
        [1,0,0,1,0,1,0,0],
        [0,0,1,0,1,0,1,0],
        [0,1,0,1,0,0,0,1],
        [1,0,1,0,0,0,1,0],
        [0,0,0,1,0,1,0,1],
        [0,1,0,0,1,0,1,0]
    ]
)

print A
print

D = np.sum(A,0)
D = np.diag(D)
print D
print 

L = D - A
print L

print np.sum(np.sum(A,0))