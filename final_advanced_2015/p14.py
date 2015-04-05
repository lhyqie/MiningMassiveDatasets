import numpy as np

V = np.array([[-0.57, -0.09],
              [-0.11, 0.7],
              [-0.57, -0.09],
              [-0.11, 0.7],
              [-0.57, -0.09]
             ])

q1 = [5,0,0,0,0]
q2 = [0,5,0,0,0]
q3 = [0,0,0,0,4]

q1_new = np.dot(q1,V)
q2_new = np.dot(q2,V)
q3_new = np.dot(q3,V)

print q1_new 
print 

print q2_new
print 

print q3_new

import matplotlib.pyplot as plt

plt.scatter(q1_new[0], q1_new[1])
plt.text(q1_new[0]+0.05, q1_new[1], '1')

plt.scatter(q2_new[0], q2_new[1])
plt.text(q2_new[0]+0.05, q2_new[1], '2')

plt.scatter(q3_new[0], q3_new[1])
plt.text(q3_new[0]+0.05, q3_new[1], '3')

plt.show()

print 'asnwer is C : [1,3] and [2]'

# B