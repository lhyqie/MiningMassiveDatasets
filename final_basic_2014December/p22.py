from p5 import cosine

def pearson_correlation(v1, v2):
    v1 = [ e - v1_mean for e in v1]
    v2 = [ e - v2_mean for e in v2]
    return cosine(v1, v2)



v1 = [0, 3, 1, 2, 0] #B 
v2 = [0, 4, 3, 0, 2] #D
print v1
print v2
print 

v1_mean = sum(v1) * 1.0 / len(v1)
v2_mean = sum(v2) * 1.0 / len(v2)
 
 
centered_v1 = [e - v1_mean if e !=0  else 0 for e in v1] 
centered_v2 = [e - v2_mean if e !=0  else 0 for e in v2]

print centered_v1
print centered_v2
print 

print 'cosine of centered v1 and v2 : ', cosine(centered_v1, centered_v2)

mean_filled_v1 = [e - v1_mean for e in v1]
mean_filled_v2 = [e - v2_mean for e in v2]

print 'pearson correlation between mean_filled v1 and v2 : ', pearson_correlation(mean_filled_v1, mean_filled_v2)

# A