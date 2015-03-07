def h(x):
    return (3 * x + 7 ) % 11

#options = [[4, 5, 6 ,7],[1,3,6,8],[2,6,8,10],[1,2,3,9]]
#options = [[1, 3, 9 ,10],[1, 3, 6 ,8],[2, 5, 7, 10],[4, 5, 6, 10]]
options = [[1, 2, 3, 9],[4, 5, 6, 10],[3, 7, 8, 10],[2, 5, 7, 10]]

for option in options:
    print option
    for e in option:
        print e, h(e), "{0:b}".format(h(e))