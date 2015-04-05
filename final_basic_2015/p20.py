"""
Consider an execution of the BALANCE algorithm with 4 advertisers, A1, A2, A3, A4, and 4 kinds of queries, Q1, Q2, Q3, Q4. 
Advertiser A1 bids on queries Q1 and Q2; A2 bids on queries Q2 and Q3; A3 on queries Q3 and Q4; and A4 on queries Q1 and Q4. 

All bids are equal to 1, and all clickthrough rates are equal.
All advertisers have a budget of 3, and ties are broken in favor of the advertiser with the lower index (e.g., A1 beats A2). 

Queries appear in the following order: 

Q1, Q2, Q3, Q3, Q1, Q2, Q3, Q1, Q4, Q1 

Which advertiser's budget is exhausted first?

 A1
 A4
 A3
 A2
"""



# C

queries = ['Q1','Q2','Q3','Q3','Q1','Q2','Q3','Q1','Q4','Q1']
advertiser2q = {'A1':set(['Q1','Q2']), 'A2':set(['Q2','Q3']), 'A3':set(['Q3','Q4']), 'A4':set(['Q1','Q4'])}
budget = {'A1':3, 'A2':3, 'A3':3, 'A4':3}

def chooseCandidate(cand_advertisers, budget):
    max_budget = 0
    for advertiser in cand_advertisers:
        if max_budget < budget[advertiser]:
            max_budget = budget[advertiser]
    candidates_with_max_budget = []
    for advertiser in cand_advertisers:
        if budget[advertiser] == max_budget:
            candidates_with_max_budget.append(advertiser)
    if len(candidates_with_max_budget) == 0:
        return None
    if len(candidates_with_max_budget) == 1:
        return candidates_with_max_budget[0]
    else: # more than one candidate with max_bugdet,   break the tie in favor of their index
        candidates_with_max_budget.sort()  # trick
        return candidates_with_max_budget[0]  

for query in queries:
    print 'query =', query, 'budget =', budget
    cand_advertisers = []
    for advertiser in advertiser2q:
        if query in advertiser2q[advertiser]:
            cand_advertisers.append(advertiser)
    #print cand_advertisers
    winner = chooseCandidate(cand_advertisers, budget)
    budget[winner] -= 1
    print winner
print 'finally budget =', budget

# C  : A3 exhausted first

    