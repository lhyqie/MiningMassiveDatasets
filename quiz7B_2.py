"""
The spam-farm architecture described in Section 5.4.1 suffers from the problem that the target page has many links --- one to each supporting page. 
To avoid that problem, the spammer could use the architecture shown below:

https://d396qusza40orc.cloudfront.net/mmds/images/otc_spamfarm1.gif

There, k "second-tier" nodes act as intermediaries. The target page t has only to link to the k second-tier pages, 
and each of those pages links to m/k of the m supporting pages. Each of the supporting pages links only to t 
(although most of these links are not shown). Suppose the taxation parameter is beta = 0.85, and x is the amount of 
PageRank supplied from outside to the target page. Let n be the total number of pages in the Web. Finally, 
let y be the PageRank of target page t. If we compute the formula for y in terms of k, m, and n, we get a formula with the form

y = ax + bm/n + ck/n
Note: To arrive at this form, it is necessary at the last step to drop a low-order term that is a fraction of 1/n. 
Determine coefficients a, b, and c, remembering that beta is fixed at 0.85. 
Then, identify the value, correct to two decimal places, for one of these coefficients.
"""

# induction is in quiz7B_2.jpg


beta =  0.85

a = 1 / (1- beta ** 3)

b = beta * (1 - beta) / (1 - beta ** 3)

c = beta ** 2  * (1 - beta) / (1 - beta ** 3)

print 'a =', a 

print 'b =', b

print 'c = ', c