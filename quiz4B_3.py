import numpy as np

X = np.array([[1,1],[2,2],[3,4]])
XT = X.T

print np.dot(X.T, X)

# hence 21