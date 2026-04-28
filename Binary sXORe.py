"""
Given a number n, define its sXORe to be 0 XOR 1 XOR 2 ... XOR n where XOR is the bitwise XOR operator.

Write a function that takes n and finds its sXORe.

        n |   sXORe n
----------|----------
        0 |         0
        1 |         1
       50 |        51
1 000 000 | 1 000 000
"""


def sxore(n):
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else:
        return 0
# Teste

print(sxore(0))  # 0
print(sxore(1))  # 1
print(sxore(50))  # 51
print(sxore(1000000))  # 1000000