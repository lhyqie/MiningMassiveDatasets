"""
    Jaccard Distance = 1 - Jaccard Similarity
    if they are equal, they must be both 0.5
    
    when x is in [3,4]    
        Jaccard similarity =  |1,2,x| /  |1,2,3,4,5,6| = 3./6 = 0.5 
    when x is in [1,2]
        Jaccard similarity =  |1,2| /  |1,2,3,4,5,6| = 2./6 = 0.333
    when x is in [5,6]
        Jaccard similarity =  |1,2| /  |1,2,3,4,5,6| = 2./6 = 0.333
    when x is outside of [1,2,3,4,5,6]
        Jaccard similarity =  |1,2| /  |1,2,3,4,5,6,x| = 2./7 = 0.2857
        
    
    so to make Jaccard similarity = 0.5, x can only be one of {3,4}
    asnwer is 2
"""

# D