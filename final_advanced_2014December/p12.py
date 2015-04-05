import numpy as np
from collections import Counter
from math import log

def entropy(X):
    counter = Counter()
    for x in X[:]:
        counter[x] += 1
    #print counter
    H = 0
    total = sum(counter.values())
    for k,v in counter.iteritems():
        p = v * 1.0 / total
        #print 'p=',p
        H += - p * log(p, 2)
    return H

def entropy_cond(data, x_col, x_vals, y_col):
    X = data[:,x_col]
    y = data[:,y_col]
    #print X, y
    #y = y[X == x_val]
    #X = X[X == x_val]
    #print X, y
    
    H_Y_X = 0
    counter = Counter()
    for x_val in X[:]:
        counter[x_val] += 1
    total = sum(counter.values())
    for x_val, count in counter.iteritems():
        p = count * 1.0 / total
        H_Y_X += p * conditional_entropy(data, x_col, x_val, y_col)
    return H_Y_X
        
    
def conditional_entropy(data, x_col, x_val, y_col):
    X = data[:,x_col]
    y = data[:,y_col]
    #print X, y
    y = y[X == x_val]
    X = X[X == x_val]
    #print X, y
    return entropy(y)



data = np.array([[1,0,1,1],
                 [0,1,1,0],
                 [0,0,0,0],
                 [1,1,1,1],
                 [1,1,0,1],
                 [0,0,0,0],
                 [1,1,1,1],
                 [0,1,0,0],
                 [1,0,1,0],
                 [1,0,1,1]])
X = data[:,:3]
y = data[:,3]
 
print X
print y
print
 
print 'H(y) = ', entropy(y)
print 

for x_col in [0, 1, 2]:    
    for x_val in [0, 1]:
        print 'H(y | x_{} = {}) = {} '.format( x_col, x_val, conditional_entropy(data, x_col, x_val, 3))

print
for x_col in [0, 1, 2]:
    print 'H(y | x_{}) = {}'.format(x_col, entropy_cond(data, x_col, [0, 1], 3)), 
    print 'H(Y) - H(y | x_{}) = {}'.format(x_col, entropy(y) - entropy_cond(data, x_col, [0, 1], 3)) 

# anwer is D
    
  