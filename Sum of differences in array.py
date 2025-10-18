"""
Your task is to sum the differences between consecutive pairs in the array in descending order.

Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).
"""

def sum_of_differences(arr):
    res = []
    arr.sort(reverse=True)
    temp = 0
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    for n in range(len(arr)):
        if (n + 1) == len(arr):
            break
        res.append(arr[n] - arr[n + 1])
    return sum(res) * -1 if sum(res) < 0 else 1

# Teste

print(sum_of_differences([-3, -2, -1]))