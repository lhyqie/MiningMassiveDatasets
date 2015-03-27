from scipy.sparse import coo_matrix
import numpy as np

name2id = {}
n = 0

line_cnt = 0
with open('web-Google.txt','r') as fr:
    for line in fr:
        line_cnt += 1
        #if line_cnt > 10000 : break
        if line.startswith('#') : continue
        tokens = line.strip().split('\t')
        #print tokens
        if tokens[0] not in name2id: 
            name2id[tokens[0]] = n
            n += 1
        
        if tokens[1] not in name2id: 
            name2id[tokens[1]] = n
            n += 1
            
print len(name2id)
print n

col = []
row = []
value = []

line_cnt = 0
with open('web-Google.txt','r') as fr:
    for line in fr:
        line_cnt += 1
        #if line_cnt > 10000 : break
        if line.startswith('#') : continue
        tokens = line.strip().split('\t')
        url1 = name2id[tokens[0]]
        url2 = name2id[tokens[1]]
        #print url1, url2
        col.append(url1)
        row.append(url2)
        value.append(1.0)

M = coo_matrix((value, (row,col)), shape=(n, n))
print M
print M.shape
print

din = M.sum(1)
print din
print din.shape
print 

dout = M.sum(0).T
print dout
print dout.shape
print 

value = [1.0 / dout[col[i], 0] for i, v in enumerate(value)]
#print value

M = coo_matrix((value, (row,col)), shape=(n, n))
print M
print M.shape
print


beta = 0.8
r = np.ones([n,1])
r = r/n
print np.sum(r) 
 
t = 1
while t < 200:
    old_r = r
    t += 1
    print 't =', t
            
    r  = beta * M * r  #+ ((1-beta) / n)
    for j in xrange(n):
        if din[j,0] == 0 :
            r[j] = 0
    
    S = r.sum()
    print 'S =', S
    r = r +  (1 - S)/n
    print 'r.sum() = ', r.sum()
     
    print 'norm of diff:', np.linalg.norm(old_r - r)
    print 'pagerank("99")', r[name2id['99']]
    print 
