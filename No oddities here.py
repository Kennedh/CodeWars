"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

def no_odds(values):
    return [a for a in values if (a % 2 == 0)]

# Teste

print(no_odds([-1, -3, -5, -7, -9, 0, 2, 4, 6, 8, 10]))
print(no_odds([2, 4, 8, 6, 0]))
print(no_odds([-42, -100, 2, 1, -147, 165, -164, -196, -167, -73, -92, 67, -104, -98]))