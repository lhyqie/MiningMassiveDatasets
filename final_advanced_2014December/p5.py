"""
let q be the reducer size
n be the total input size
no reducer can cover q * (q-1) * (q-2) / (3 * 2 * 1) outputs  ~= q^3 / 6
total possible inputs should be covered is n * (n-1) * (n-2) / (3 * 2 * 1)  ~= n^3 / 6
# of reducers needed p =  (n^3 / 6)  / (q^3 / 6)  = n^3 / q^3

according to r = pq/I  where I is n

r =  (n^3 / q^3) * q / n = n^2 / q^2

answer is A 
"""