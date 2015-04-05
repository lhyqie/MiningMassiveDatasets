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
        
Xs = [9, 15, 16, 23, 25, 27, 28, 56]

from collections import defaultdict,Counter

combiner = defaultdict(list)

for i, x in enumerate(Xs):
    Ys = findPrimeDivisors(x)
    mapper_id = i/2 
    for y in Ys:
        print 'mapper_id : ', mapper_id,  ' \t (k,v) : ', (y, x)
        combiner[mapper_id].append((y, x))

print 

num_tuples_for_reducer = 0

for mapper_id in combiner:
    print mapper_id, combiner[mapper_id]
    counter = Counter()
    for k, v in combiner[mapper_id]:
        counter[k] += v
    print counter
    print 
    
    num_tuples_for_reducer += len(counter)

print 'asnwer is :', num_tuples_for_reducer

#  B

