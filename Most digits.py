"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
"""

def find_longest(arr):
    arr = [str(a) for a in arr]
    return int(max(arr, key=len))

# Teste

print(find_longest([1, 10, 100]))
print(find_longest([9000, 8, 800]))
print(find_longest([8, 900, 500]))
print(find_longest([3, 40000, 100]))
print(find_longest([1, 200, 100000]))