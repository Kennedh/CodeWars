"""
In this Kata your task will be to return the count of pairs that have consecutive numbers. The first pair consists of
the first and second element of the input, the second pair is the next two elements (3rd and 4th), etc. If the input
ends with an element without a pair, it should be ignored.

For example, [1,2,5,8,-4,-3,7,6,5] has 3 such pairs. Candidate pairs are selected as follows: [(1,2), (5,8), (-4,-3),
(7,6), 5].

the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
the second pair is (5,8) and the numbers are not consecutive.
the third pair is (-4,-3), consecutive. Count = 2.
the fourth pair is (7,6), also consecutive. Count = 3.
the last element has no pair, so we ignore.
Good luck!
"""

def pairs(arr):
    count = 0
    for i in range(0, len(arr) - 1, 2):
        if abs(arr[i] - arr[i + 1]) == 1:
            count += 1
    return count

# Teste

print(pairs([1,2,5,8,-4,-3,7,6,5]))
print(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]))
print(pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]))