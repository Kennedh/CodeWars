"""
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]

"""

def pyramid(n):
    temp = []
    res  = []
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    for y in range(n):
        for x in range(y + 1):
            temp.append(1)
        res.append(temp)
        temp = []
    return res

# Teste

print(pyramid(3))