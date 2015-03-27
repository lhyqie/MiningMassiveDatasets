from math import sqrt
y = [2., 3., 5.]
y_est = [1., 4., 5.]

def RMSE(y, y_est):
    res = 0.0
    for i in xrange(len(y)):
        res += (y[i] - y_est[i]) ** 2
    return sqrt(res)

print RMSE(y,y_est)
print 'aswner is D'