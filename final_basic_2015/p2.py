data = [(1,0),
(2,1),
(3,0),
(4,1),
(5,0)]

def hash(x):
    return (3 * x + 2) % 11

print data

minhash = 1000
for r, c in data:
    print r, c, hash(r)
    if c == 1:
        if minhash > hash(r):
            minhash = hash(r)
    
print 'minhash is :', minhash

# C