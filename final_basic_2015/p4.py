"""
In this market-basket problem, there are 99 items, numbered 2 to 100. There is a basket for each
prime number between 2 and 100. The basket for p contains all and only the items whose
numbers are a multiple of p. For example, the basket for 17 contains the following items: {17, 34,
51, 68, 85}. What is the support of the pair of items {12, 30}?
"""


from collections import defaultdict
baskets = defaultdict(list)
primes = []

def isPrime(x):
    for i in xrange(2,x):
        if x % i == 0: return False
    return True

for i in xrange(2,101):
    if isPrime(i):
        primes.append(i)
print primes
print 

for i in xrange(2,101):
    for prime in primes:
        if i % prime == 0 :
            baskets[prime].append(i)

for basket, items in baskets.iteritems():
    print basket, ':', items
    
print '(eyeball it) answer is 2'


# A