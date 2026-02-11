"""
Rick wants a faster way to get the product of the largest pair in an array. Your task is to create a performant
solution to find the product of the largest two integers in an array of positive numbers.

Rick is only interested in solutions that are faster than his, which has a running time of O(n log n).

[2, 6, 3]                      => 18 = 6 * 3
[2, 1, 5, 0, 4, 3]             => 20 = 5 * 4
[7, 8, 9]                      => 72 = 8 * 9
[33, 231, 454, 11, 9, 99, 57]  => 104874 = 231 * 454
"""

def max_product(a):
    frst_max = 0
    lst_max  = 0
    for num in a:
        if num > frst_max:
            lst_max = frst_max
            frst_max = num
        elif num > lst_max:
            lst_max = num
    return frst_max * lst_max


# Teste

print(max_product([2, 6, 3]))
print(max_product([2, 1, 5, 0, 4, 3]))
print(max_product([7, 8, 9]))
print(max_product([33, 231, 454, 11, 9, 99, 57]))