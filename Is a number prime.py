"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer
is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other
than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
"""


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limite = int(num ** 0.5) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            return False

    return True


# Testes
print(is_prime(2))
print(is_prime(3))
print(is_prime(17))
print(is_prime(15))
print(is_prime(1))
print(is_prime(0))
print(is_prime(-5))
print(is_prime(997))