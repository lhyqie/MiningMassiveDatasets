"""
My answer is not exactly the same, but it is very close.
Don't know where the bug is , given the difference is small, the bug rarely occurs

You entered:

Your Answer        Score    Explanation
428827354    Incorrect    0.00    The right answer is 42949****, so you are close. If you are using bands, try changing the size of them.
Total        0.00 / 1.00

"""
def sample_file():
    fw = open('sentences_sample.txt','w')
    line_cnt = 0
    with open('sentences.txt','r') as fr:
        for line in fr:
            fw.write(line)
            line_cnt += 1
            if line_cnt > 300000:
                break
            
def convert2Int(origin_filepath, target_filepath):
    word2id = {}
    cnt = 0
    with open(origin_filepath,'r') as fr:
        for line in fr:
            tokens = line.strip().split(' ')
            #print len(tokens)
            for word in tokens[1:]:
                if word not in word2id:
                    word2id[word] = cnt
                    cnt += 1
    #print word2id
    fw = open(target_filepath, 'w')
    with open(origin_filepath,'r') as fr:
        for line in fr:
            tokens = line.strip().split(' ')
            fw.write(tokens[0]+' ')
            for word in tokens[1:]:
                fw.write(str(word2id[word])+' ')
            fw.write('\n')

def constructMatrix(filepath):
    y = []
    from scipy.sparse import coo_matrix
    from collections import Counter
    col = []
    row = []
    val = []
    with open(filepath,'r') as fr:
        line_cnt = 0
        for line in fr:
            line_cnt += 1
            if line_cnt % 1000 == 0 : print line_cnt
            line = line.strip()
            #print line
            tokens = line.split(' ')
            y.append(tokens[0])
            word2cnt = Counter()
            for token in tokens[1:]:
                word2cnt[token] += 1
            for word in word2cnt:
                col.append(word)
                row.append(tokens[0])
                val.append(word2cnt[word])
    X = coo_matrix((val, (row,col)), dtype=complex)
    return X, y

def split_sentences():
    from collections import defaultdict
    length2docs = defaultdict(list)
    line_cnt = 0
    with open('sentences_int.txt', 'r') as fr:
        for line in fr:
            line_cnt += 1
            if line_cnt % 10000 == 0:
                print line_cnt
            length = len(line.strip().split()) - 1
            length2docs[length].append(line)
    for length in length2docs:
        print length, len(length2docs[length])
        with open('docs/'+str(length)+'.txt','w') as fw:
            for line in length2docs[length]:
                fw.write(line)

def loadSentencesFromOneFile(filepath):
    sents = {}
    try:
        with open(filepath, 'r') as fr:
            for line in fr:
                tokens = line.strip().split(' ')
                sents[tokens[0]] = map(int, tokens[1:])
    except IOError:
        return {}
    return sents 

def loadSentencesFromTwoFiles(length):
    sents1 = loadSentencesFromOneFile('docs/'+str(length)+'.txt')
    sents2 = loadSentencesFromOneFile('docs/'+str(length+1)+'.txt')
    sents = {}
    for sent in sents1:
        sents[sent] = sents1[sent]
    for sent in sents2:
        sents[sent] = sents2[sent]
    return sents

def hash1(sent):
    return sum(sent[:len(sent)/2])  

def hash2(sent):
    return sum(sent[len(sent)/2:])

def pairsFromBuckets(buckets):
    pairs = set()
    for hashcode, docnames in buckets.iteritems():
        sorted_docnames = sorted(docnames)
        for i in xrange(len(sorted_docnames)):
            for j in xrange(i+1, len(sorted_docnames)):
                pairs.add( (sorted_docnames[i], sorted_docnames[j]))
    return pairs

def editdistanceLessThanOne(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    n1 = len(s1)
    n2 = len(s2)
    if n2 - n1 > 1:
        return False
    # find the offset (pos1) from the left,  where s1[pos1] != s2[pos1]
    pos1 = 0
    while pos1 < n1 :  # given that n1 == n2 or n1 == n2- 1
        if s1[pos1] == s2[pos1]:
            pos1 += 1
        else:
            break
    if pos1 == n1:
        #print 'pos1 =', pos1
        return True  # s1 and s2 is exactly the same or s2 is created by concatenate one element to s1
    # find the offset from the right
    pos2 = 0
    while pos2 < n1:
        if s1[n1 - 1 - pos2] == s2[n2 - 1 - pos2]:
            pos2 += 1
        else:
            break
    #print 'pos1 =', pos1, 'pos2=', pos2,  'n1 - 1 - pos2 = ', n1 - 1 - pos2
    if pos1 < n2 - 1 - pos2:
        return False        
    return True
    
def levenshteinDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def findSimilarPairs(length):
    simPairs = set()
    sents = loadSentencesFromTwoFiles(length)
    #print len(sents)
    #for name in sents:
    #    print name, sents[name]
    from collections import defaultdict
    buckets1 = defaultdict(list)
    buckets2 = defaultdict(list)
    cnt = 0
    for name, sent in sents.iteritems():
        #print name, sent
        cnt += 1
        if cnt % 100000 == 0 : print '.', 
        buckets1[hash1(sent)].append(name)
        buckets2[hash2(sent)].append(name)
    
    #for hc in buckets1:
    #    if len(buckets1[hc]) > 10:  
    #        print name, len(buckets1[hc]) * (len(buckets1[hc]) - 1) / 2
        
    #for hc in buckets2:
    #    if len(buckets2[hc]) > 10:  
    #        print name, len(buckets2[hc]) * (len(buckets2[hc]) - 1) / 2
    
    pairs1 = pairsFromBuckets(buckets1)
    pairs2 = pairsFromBuckets(buckets2)
    all_pairs = pairs1.union(pairs2)
    print 'len(pairs1)=', len(pairs1)
    print 'len(pairs2)=', len(pairs2)
    print 'len(all_pairs)=', len(all_pairs)
    cnt = 0
    for pair in all_pairs:
        cnt += 1
        if cnt % 100000 == 0 : print cnt,
        if cnt % 1000000 == 0: print 
        #print pair
        #diff = levenshteinDistance(sents[pair[0]], sents[pair[1]])
        #print diff  
        #if diff == 1:
        #    print sents[pair[0]]
        #    print sents[pair[1]]
        #if diff <= 1:
        #    simPairs.add(pair)
        if editdistanceLessThanOne(sents[pair[0]], sents[pair[1]]):
            simPairs.add(pair)
    #for e in buckets1[33839]:
    #    print e, sents[e]
    
    #print sents['1289717']
    #print sents['551432']
    #print levenshteinDistance(sents['1289717'], sents['551432'])
    return simPairs

def writeSimPairs(simPairs, length):
    with open('pairs/'+str(length)+'.txt','w') as fw:
        for pair in simPairs:
            fw.write(pair[0]+' '+pair[1]+'\n')

def getLengths():
    import os
    lengths = []
    for file in os.listdir('docs'):
        if file.endswith('.txt'):
            file = file[:-4]
            lengths.append(int(file))
    
    lengths.sort()
    return lengths

def genPairs():
    lengths = getLengths()
    skip = 0
    for length in lengths[skip:]:
        print '-------------------------------- length =', length, '----------------------------------------------'           
        simPairs = findSimilarPairs(length)
        writeSimPairs(simPairs,length)
    
def computeFinalResult():
    lengths = getLengths()
    all_pairs = set()
    for length in lengths:
        print 'length =', length
        with open('pairs/'+str(length)+ '.txt', 'r') as fr:
            line_cnt = 0
            for line in fr:
                line_cnt += 1
                if line_cnt % 100000 == 0: print '.',
                if line_cnt % 5000000 == 0: print 
                all_pairs.add(tuple(line.strip().split(' ')))
            print 'total # of row = ', line_cnt
            print 'size of all_pairs =', len(all_pairs)
            
    
# ------------------------------------------ main -------------------------------------------
if __name__ == '__main__':    
    #sample_file()
    #convert2Int('sentences_sample.txt', 'sentences_int_sample.txt')
    #convert2Int('sentences.txt', 'sentences_int.txt')
    #split_sentences()
    #genPairs()
    computeFinalResult()
    
        

    
#     def loadPairs(filepath):
#         pairs = set()
#         with open(filepath,'r') as fr:
#             for line in fr:
#                 pairs.add(tuple(line.strip().split(' ')))
#         return pairs
#      
#     sents = loadSentencesFromTwoFiles(10)
#     pairs1 = loadPairs('pairs/10.txt')
#     pairs2 = loadPairs('pairs/10_old.txt')
#      
#     for pair in pairs2.difference(pairs1):
#         print pair
#         print sents[pair[0]]
#         print sents[pair[1]]
#         print ----------- 

    
    """
    X, y = constructMatrix('sentences_int_sample.txt')
    #X, y = constructMatrix('sentences_int.txt')
    print X.shape, len(y)
    
    from sparselsh.lsh import LSH
    lsh = LSH( 8,
               X.shape[1],
               num_hashtables=1,
               storage_config={"dict":None})
    for ix in xrange(X.shape[0]):
        x = X.getrow(ix)
        c = y[ix]
        lsh.index( x, extra_data=c)
        if ix % 100 == 0 : print ix
    for e in lsh.query(X.getrow(0), num_results=3):
        print e[0], e[1]
    """
