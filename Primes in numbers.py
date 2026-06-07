"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following
form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1
    if n > 1:
        factors.append((n, 1))

    result = []
    for p, exp in factors:
        if exp == 1:
            result.append(f"({p})")
        else:
            result.append(f"({p}**{exp})")
    return "".join(result)

# Teste

print(prime_factors(7775460))
print(prime_factors(7919))
