"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string
'(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>,
String> in Rust).

Examples:
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""


def divisors(n):
    res = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    divisors_list = sorted(res)
    if not divisors_list:
        return f"{n} is prime"
    return divisors_list

# Teste

print(divisors(15))
print(divisors(253))
print(divisors(24))
print(divisors(25))

