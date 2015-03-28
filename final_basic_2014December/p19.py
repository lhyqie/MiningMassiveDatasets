"""
centroid  (c1, c2, c3)
        where c_i = SUM_i/n
deviation (sigma_1, sigma_2, sigma_3)
        where sigma_i ^ 2 =  (SUMSQ_i/ n )  -  (SUM_i/ n) ^2
Mahalanobis distance of  point P (p1, p2, p3) to centroid 
   is sqrt( sum_i{ ( (p_i - c_i) / (sigma_i) ) ^2  }  )
    = sqrt( sum_i{   (p_i - c_i)^2 / (sigma_i)^2  }  )
    = sqrt( sum_i{   (p_i - SUM_i/n)^2 / ((SUMSQ_i/ n )  -  (SUMS_i/ n) ^2)    }  )
"""

from math import sqrt

n = 1000
SUM = (-323., 1066., 1776.)
SUMSQ = (412., 1500., 3500.)
P = (0.,0.,0.)

centroid = [e/ n for e in SUM]
std = [ sqrt(SUMSQ[i]/n - (SUM[i]/n)**2) for i in range(len(SUM))]

print centroid
print std


y = [ (P[i] - centroid[i]) / std[i]  for i in range(len(P))]

print y

sum = 0
for e in y:
    sum += e * e

print 'asnwer is :', sqrt(sum)
# C