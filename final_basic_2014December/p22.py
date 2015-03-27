from p5 import consine

def pearson_correlation(v1, v2):
    v1_mean = sum(v1) * 1.0 / len(v1)
    v2_mean = sum(v2) * 1.0 / len(v2)
    v1 = [ e - v1_mean for e in v1]
    v2 = [ e - v2_mean for e in v2]
    return consine(v1, v2)



v1 = [0, 3, 1, 2, 0] #B 
v2 = [0, 4, 3, 0, 2] #D

#  do we need fill the blank with average?
#v1 = [11./3, 3, 1, 2, 3./2] #B 
#v2 = [11./3, 4, 3, 12./3, 2] #D

print pearson_correlation(v1, v2)

from scipy.stats.stats import pearsonr
print pearsonr(v1,v2)