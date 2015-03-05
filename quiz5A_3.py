from math import sqrt

x = (0,0)
y = (10,10)
a = (1,6)
b = (3,7)
c = (4,3) 
d = (7,7) 
e = (8,2) 
f = (9,5)

def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

points = [a, b, c, d, e, f]
centroids = [x, y]

from matplotlib import pyplot as plt
plt.scatter( zip(*(points+centroids))[0], zip(*(points+centroids))[1]) 

while len(points) > 0:
    max_dist = 0
    max_i = -1
    for i, point in enumerate(points):
        dist_temp = []
        for centroid in centroids:
            dist_temp.append(dist(point, centroid))
        if min(dist_temp) > max_dist:
            max_dist = min(dist_temp)
            max_i = i
        print i, min(dist_temp)
    
    centroids.append(points[max_i])
    points.pop(max_i)
    print centroids
    print points
    print '----------------------------------'
    
plt.show()