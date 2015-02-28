from numpy import dot
from numpy.linalg import norm

# a = [.954, .728, -.682]
# b = [.890, -.346, -.297]
# c = [-.937, .312, .156]
# d = [2.250, -.500, -.750]
#options = [a, b , c, d]

options = [
[-.548, .401, .273],
[.608, -.459, -.119],
[.702, -.702, .117],
[.312, .156, -.937],
]
base1 = [2./7,3./7,6./7]



for option in options:
    print option, dot(base1, option), norm(option)
    