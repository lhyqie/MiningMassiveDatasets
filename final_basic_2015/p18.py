from math import sqrt, fabs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# answer is B

points = [(1,1), (2,1), (2,2), (3,3), (4,2), (2,4), (4,4)]
centroids = [(1,1), (4,4)]

def plot():
    plt.figure()
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    
    x2 = [point[0] for point in centroids]
    y2 = [point[1] for point in centroids]

    plt.scatter(x, y, c='yellow')
    plt.scatter(x2, y2, c='green', marker='x')
    for i in xrange(len(points)):
        plt.plot([points[i][0],centroids[S[i]][0]], [points[i][1], centroids[S[i]][1]],color='b')

    
def dist(p1, p2):
    return fabs(p1[0] - p2[0]) + fabs(p1[1] - p2[1])
    #return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def updateDistance(D, points, centroids):
    for i in xrange(len(points)):
        for j in xrange(len(centroids)):
            D[i,j] = dist(points[i], centroids[j])

def updateCentroids(S, points, centroids):
    for j in xrange(len(centroids)):
        cx = 0.
        cy = 0.
        cnt = 0
        for i in xrange(len(points)):
            if S[i] == j:
                cx += points[i][0]
                cy += points[i][1]
                cnt += 1
        centroids[j] = (cx/cnt, cy/cnt)
    
# distance matrix
D = np.zeros([len(points), len(centroids)])
updateDistance(D, points, centroids)
print 'Distance Matrix D =', D
print

# ---------------------------------------------------
# cluster assignment 
S = np.argmin(D, axis=1)
old_S = S
print 'cluster assignment S =', S
print

plot()
# update centroids
updateCentroids(S, points, centroids)
print 'centriods =', centroids
print

# update distance
updateDistance(D, points, centroids)
print 'Distance Matrix =', D
print

# ---------------------------------------------------
# cluster assignment 
S = np.argmin(D, axis=1)
print 'cluster assignment S =', S
print

plot()
# update centroids
updateCentroids(S, points, centroids)
print 'centriods =', centroids
print

# update distance
updateDistance(D, points, centroids)
print 'Distance Matrix =', D
print

for i in xrange(len(points)):
    if S[i] != old_S[i]:
        print points[i]

print centroids

plt.show()


# C   (13./4, 13./4)