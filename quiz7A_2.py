data = {
's1':'abcef',
's2':'acdeg',
's3':'bcdefg',
's4':'adfg',
's5':'bcdfgh',
's6':'bceg',
's7':'cdfg',
's8':'abcd',
}

J = 0.2 # jaccard distance

from collections import defaultdict
letter2word = defaultdict(list)

for k, v in data.iteritems():
    preLen = int(len(v) * J + 1)
    chs = v[:preLen]
    #print preLen, chs
    for ch in chs:
        letter2word[ch].append({k:v})
        

for k, v in letter2word.iteritems():
    print k, v