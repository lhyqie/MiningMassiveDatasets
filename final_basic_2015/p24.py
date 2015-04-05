"""
We are going to perform a hierarchical (agglomerative) clustering on the four strings {he, she,
her, their}, using edit distance (just insertions and deletions; no mutations of characters). Initially,
each string is in a cluster by itself. The distance between two clusters is the minimum edit
distance between two strings, one chosen from each of the two clusters. When we complete the
hierarchical clustering, there is one cluster containing all four strings, and we performed three
mergers of clusters to get to that point. For each of the three mergers there was a distance
between the merged clusters. What is the sum of those three distances?
3
"""

def edit_distance(s1, s2): 
    """just insertions and deletions *no mutation*
    """
    n1 = len(s1)+1
    n2 = len(s2)+1
    m = [[0 for _ in range(n2)] for _ in range(n1)]
    for i in xrange(n1):
        m[i][0] = i
    for j in xrange(n2):
        m[0][j] = j
    for i in xrange(1,n1):
        for j in xrange(1,n2):
            if s1[i-1] != s2[j-1]:
                m[i][j] = min(m[i-1][j], m[i][j-1]) + 1
            else:
                m[i][j] = m[i-1][j-1]
    #print
    #for i in range(n1):
    #    for j in range(n2):
    #        print m[i][j],
    #    print
    return m[n1-1][n2-1]

words = ['he', 'she', 'her', 'their']
for i in xrange(len(words)):
    for j in xrange(i+1, len(words)):
        print words[i], words[j], edit_distance(words[i], words[j])       
        print     
        
#---- begin clustering----
clusters = [ [word] for word in words]

def pickTwoCluster(cluters):
    cid1 = None
    cid2 = None
    min_distance_overall = 1000000
    for i in xrange(len(clusters)):
        for j in xrange(i+1, len(clusters)):
            cluster1 = clusters[i]
            cluster2 = clusters[j]
            min_distance = 100000
            for s1 in cluster1:
                for s2 in cluster2:
                    distance = edit_distance(s1, s2)
                    if distance < min_distance:
                        min_distance = distance
            if min_distance < min_distance_overall:
                min_distance_overall = min_distance
                cid1 = i
                cid2 = j
    return cid1, cid2, min_distance_overall

sum_distance = 0
while len(clusters) > 1:
    cid1, cid2, distance = pickTwoCluster(clusters)
    #print cid1 , cid2
    cluster2 = clusters.pop(cid2) # pop larger index first
    cluster1 = clusters.pop(cid1)
    clusters.append(cluster1+cluster2)
    print 'cluster to merge : ', cluster1, cluster2, 'distance =', distance
    sum_distance += distance
    print 'clusters : ', clusters
    print 
    
print 'answer is :' , sum_distance