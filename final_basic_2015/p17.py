def isPrime(x):
    for i in xrange(2,x):
        if x % i == 0: return False
    return True
    
def findPrimeDivisors(x):
    res = []
    for i in range(2, x+1):
        if isPrime(i) and x % i == 0:
            res.append(i)
    return res

def mapper(Xs):
    for x in Xs:
        Ys = findPrimeDivisors(x)
        for y in Ys:
            yield (y, x)

def reducer(kv_list):
    from collections import Counter    
    counter = Counter()
    for k, v in kv_list:
        counter[k] += v
    return counter
        
Xs = [9, 15, 16, 23, 25, 27, 28, 56]

kv_list = []
for y, x in mapper(Xs):
    kv_list.append((y, x))
for k, v in kv_list:
    print k,v 
counter = reducer(kv_list)

print 
for k, v in counter.iteritems():
    print k, v     

# answer is B (3, 51)
