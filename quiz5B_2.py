import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from math import sqrt

def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def drawRect(ax, UL, LR, color):
    verts = [
    (UL[0], UL[1]), # upper left
    (UL[0], LR[1]), # lower left
    (LR[0], LR[1]), # lower right
    (LR[0], UL[1]), # upper right
    (UL[0], UL[1]), # ignored
    ]
    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=color, lw=2)
    ax.add_patch(patch)



ab = (5, 10)
cd = (20, 5)

#ULs1 = [(7,8),(7,12),(6,7),(6,7)]
#LRs1 = [(12,5),(12,8),(11,4),(11,4)]
#ULs2 = [(15,14),(16,19),(14,10),(11,5)]
#LRs2 = [(20,10),(25,12),(23,6),(17,2)]

#ULs1 = [(3,3),(6,15),(3,3),(7,12)]
#LRs1 = [(10,1),(13,7),(10,1),(12,8)]
#ULs2 = [(15,14),(16,16),(13,10),(16,19)]
#LRs2 = [(20,10),(18,5),(16,4),(25,12)]

ULs1 = [(7,8),(6,7),(3,3),(3,15)]
LRs1 = [(12,5),(11,4),(10,1),(13,7)]
ULs2 = [(15,14),(11,5),(15,14),(14,10)]
LRs2 = [(20,10),(17,2),(20,10),(23,6)]

fig = plt.figure()

for i in xrange(len(ULs1)):
    UL1 = ULs1[i]
    LR1 = LRs1[i]
    UL2 = ULs2[i]
    LR2 = LRs2[i]
    print '----------------------------- i = {}-----------------------------'.format(i)
    print UL1, LR1, UL2, LR2
    print 'dist(ab,UL1) = ', dist(ab, UL1), 'dist(cd,UL1) = ', dist(cd, UL1)
    print 'dist(ab,UR1) = ', dist(ab, (LR1[0], UL1[1])), 'dist(cd,UR1) = ', dist(cd, (LR1[0], UL1[1]))
    print 'dist(ab,LL1) = ', dist(ab, (UL1[0], LR1[1])), 'dist(cd,LL1) = ', dist(cd, (UL1[0], LR1[1]))
    print 'dist(ab,LR1) = ', dist(ab, LR1), 'dist(cd,LR1) = ', dist(cd, LR1)
   
    print '-------'
    print 'dist(ab,UL2) = ', dist(ab, UL2), 'dist(cd,UL2) = ', dist(cd, UL2)
    print 'dist(ab,UR2) = ', dist(ab, (LR2[0], UL2[1])), 'dist(cd,UR2) = ', dist(cd, (LR2[0], UL2[1]))
    print 'dist(ab,LL2) = ', dist(ab, (UL2[0], LR2[1])), 'dist(cd,LL2) = ', dist(cd, (UL2[0], LR2[1]))
    print 'dist(ab,LR2) = ', dist(ab, LR2), 'dist(cd,LR2) = ', dist(cd, LR2)
    print 
    
    ax = fig.add_subplot(2, 2, i)
    ax.plot(ab[0], ab[1], 'o')
    ax.plot(cd[0], cd[1], 'o')
    drawRect(ax, UL1, LR1, color = 'orange')
    drawRect(ax, UL2, LR2, color = 'green')
    ax.set_xlim(0,30)
    ax.set_ylim(0,30)
    ax.set_title('fig'+str(i))

plt.show()