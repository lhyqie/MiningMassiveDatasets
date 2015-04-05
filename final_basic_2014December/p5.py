#To two decimal places, what is the cosine of the angle between the vectors [2,1,1] and [10,-7,1]?
from math import sqrt

def cosine(v1, v2):
    if len(v1) != len(v2): raise Exception('dim not match')
    dotprod = 0
    for i in xrange(len(v1)):
        dotprod += v1[i] * v2[i]
    norm1 = sqrt(sum([e**2 for e in v1]))
    norm2 = sqrt(sum([e**2 for e in v2]))
    #print dotprod, norm1, norm2
    return dotprod / (norm1 * norm2)

if __name__ == '__main__':
    print 'answer is ', cosine([2,1,1], [10,-7,1])
