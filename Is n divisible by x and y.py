"""
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero
numbers.
"""

def is_divisible(n,x,y):
    return True if n % x == 0 and n % y == 0 else False

# Teste

print(is_divisible(3,2,2))
print(is_divisible(3,3,4))
print(is_divisible(12,3,4))
print(is_divisible(8,3,4))
