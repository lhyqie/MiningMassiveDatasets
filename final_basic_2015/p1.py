"""
How many distinct 3-shingles are there in the string "hello world"? (Note: the quotes are not part
of the string.
"""


astr =  "hello world"
k = 3

shinglesSet = set()
for i in xrange(len(astr)):
    if len(astr[i:i+k]) ==  k:
        print astr[i:i+k]
        shinglesSet.add(astr[i:i+k])
        
print
print 'answer is :', len(shinglesSet)

# A