from math import exp

budget = 100

data = [ {'advertiser':'A', 'bid': 1.0, 'spend': 20.0}, 
         {'advertiser':'B', 'bid': 2.0, 'spend': 40.0},
         {'advertiser':'C', 'bid': 3.0, 'spend': 60.0},
         {'advertiser':'D', 'bid': 4.0, 'spend': 80.0}]

def psi(obj):
    bid = obj['bid']
    spend = obj['spend']
    f = 1 - spend / budget
    return bid * (1-exp(-f))

for obj in data:
    print obj, psi(obj)

# answer is A:   which is advertiser C