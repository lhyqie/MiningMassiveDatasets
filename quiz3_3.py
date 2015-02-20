curTS = 75

#options = [[37, 46, 55], [30, 47, 62], [14, 35, 42], [3, 45, 72]]
#options = [[31, 32, 44], [31, 48, 50], [4, 31, 72], [24, 44, 65]]
options = [[5, 33, 67], [30, 47, 62], [31, 48, 50], [17, 43, 51]]

for option in options:
    print option
    avg = 0.0
    for e in option:
        a = e % 10
        n = curTS - e + 1
        m = (n -1)/ 10 + 1
        print e, a, n, m, m**2 
        avg += m ** 2
    print avg / len(option)
    print
        
print 
res = 0.0
for i in range(1, curTS+1):
    res += (i % 10) ** 2
print res/curTS

# choose D 27.0 is closest to 27.33