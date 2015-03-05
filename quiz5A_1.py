import numpy as np
M = np.array([[1,0,0],[0,2,0],[0,0,0]])
print M
print 

MpInv = np.linalg.pinv(M)
print MpInv
print
