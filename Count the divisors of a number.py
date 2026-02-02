"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000, but fixed tests go higher.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to
see which numbers are counted in each case.
"""


def divisors(n):
    count = 1
    i = 2
    exp = 0
    while n % 2 == 0:
        exp += 1
        n //= 2
    count *= (exp + 1)
    i = 3
    while i * i <= n:
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        if exp > 0:
            count *= (exp + 1)
        i += 2
    if n > 1:
        count *= 2
    return count


# Testes

print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))