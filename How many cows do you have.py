"""
Consider having a cow that gives a child every year from her fourth year of life on and all her subsequent children do
the same.

After n years how many cows will you have?

After n years	Cow count
0	1
1	1
3	2
4	3
10	28
Return null if n is not an integer.

Note: Assume all the cows are alive after n years.
"""


def count_cows(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n <= 2:
        return 1
    a, b, c, d = 1, 1, 1, 2
    if n == 3:
        return d
    for year in range(4, n + 1):
        next_val = d + b
        a, b, c, d = b, c, d, next_val
    return d

# Teste

print(count_cows(1))
print(count_cows(3))
print(count_cows(5))
print(count_cows(20))