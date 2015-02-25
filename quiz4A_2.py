import numpy as np
from scipy.spatial.distance import cosine

def applyScalar(v, alpha):  v[-1] *= alpha
   
for alpha in [0, 0.5, 1, 2]:
    print '------------------------------------------------'
    print 'alpha =', alpha
    vA = np.array([1,0,1,0,1,2])
    print vA
    vB = np.array([1,1,0,0,1,6])
    print vB
    vC = np.array([0,1,0,1,0,2])
    print vC
    print 
    
    applyScalar(vA, alpha)
    applyScalar(vB, alpha)
    applyScalar(vC, alpha)
    print vA
    print vB
    print vC
    
    print 'A<->B', cosine(vA, vB)
    print 'A<->C', cosine(vA, vC)
    print 'B<->C', cosine(vB, vC)