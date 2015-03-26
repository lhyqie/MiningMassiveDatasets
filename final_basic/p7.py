"""
Suppose we have a (.4, .6, .9, .1)-sensitive family of functions. If we apply a 3-way OR
construction to this family, we get a new family of functions whose sensitivity is:
"""



a = 1 - (1 - 0.9) ** 3
b = 1 - (1 - 0.1) ** 3


print 'a =', a, 'b =', b