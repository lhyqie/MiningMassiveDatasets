import numpy as np

q1 = np.array([5,0,0,0,0])
q2 = np.array([0,2,0,0,4])

print q1
print 
print q2
print

V = np.array([  [-0.57, -0.09],
                [-0.11, 0.7],
                [-0.57, -0.09],
                [-0.11, 0.7],
                [-0.57, -0.09]  
             ]   )

q1_concept = np.dot(q1, V)
print q1_concept
print 

q2_concept = np.dot(q2, V)
print q2_concept
print 

from p5 import cosine
print cosine(q1_concept, q2_concept)

# 0.852093111886 -> 0.85