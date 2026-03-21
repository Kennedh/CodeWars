"""
Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.
"""

def largest_pair_sum(numbers):
    num1 = max(numbers)
    numbers.remove(max(numbers))
    num2 = max(numbers)
    return num1 + num2

# Teste

print(largest_pair_sum([10,14,2,23,19]))
print(largest_pair_sum([-100,-29,-24,-19,19]))
print(largest_pair_sum([1,2,3,4,6,-1,2]))
