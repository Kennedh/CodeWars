"""
Implement a function that takes two numbers m and n and returns an array of the first m multiples of the real number n.
Assume that m is a positive integer.

Ex.

(3, 5.0) --> [5.0, 10.0, 15.0]
"""

def multiples(m: int, n: int | float) -> list[int] | list[float]:
    return [a * n for a in range(1, m + 1)]

# Teste

print(multiples(3, 5))
print(multiples(1, 3.14))
print(multiples(5, -1))
