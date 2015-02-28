from numpy import dot

# options = [
#     [1, -2, 1],
#     [0, 2, -1],
#     [-1, -2, -3],
#     [-1, -2, 0]
# ]

options = [
[-1, 1, -1],
[-1, -1, 1],
[1, 1/2, 1/3],
[-1, -2, -3],
]
v = [1, 2, 3]

for option in options:
    print option, dot(v, option)