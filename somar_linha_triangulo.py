"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1)
"""

def row_sum_odd_numbers(n):
    summ = 0
    first = n ** 2 - (n - 1)
    for num in range(first, first + (2 * n), 2):
        summ += num
    return summ

# Teste

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))