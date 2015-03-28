# 3 bands
# each band 2 rows

# prob(agreement in a band) = 0.6 * 0.6
# prob(at least one agreement in 3 bands) = 1 - ( 1- 0.6 * 0.6) ^ 3


print 'answer is ',   1 - ( 1- 0.6 * 0.6) ** 3