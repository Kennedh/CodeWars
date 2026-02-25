"""
Task
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once
(ignore duplicates). Only positive integers in the range of 1 to 9 will be passed to the function.

Examples
[1, 3, 1] ==> 13
[5, 7, 5, 9, 7] ==> 579
[1, 9, 3, 1, 7, 4, 6, 6, 7]  ==> 134679
"""

def min_value(digits):
    return int("".join(map(str,sorted(set(digits)))))

# Teste

print(min_value([1, 3, 1]))
print(min_value([5, 7, 5, 9, 7]))
print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))