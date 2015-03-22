N = 10** 9 

#Each introvert page will appear as the source node in exactly one stripe of M, while the extrovert nodes appear in all stripes.

for k in [2, 3]:
    for x in [0.5, 0.75]:
        # r_new for 1 time and r_old for k times : (k+1) * N * 4
        # Introvert pages    (20 * 4 +  3 * 4) * N * x
        # extravert pages    (20.0 /k * 4 +  3 * 4) * k * N * (1-x)  
        
        IO = (k+1) * N * 4 + (20 * 4 +  3 * 4) *  N * x +  (20.0 /k * 4 +  3 * 4) * k * N * (1-x)  
        print 'N = {}, k = {}, x = {}, IO = {}GB'.format(N, k, x, IO/10**9)
        