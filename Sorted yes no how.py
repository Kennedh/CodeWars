"""
Complete the method which accepts an array of integers, and returns one of the following:

"yes, ascending" - if the numbers in the array are sorted in an ascending order
"yes, descending" - if the numbers in the array are sorted in a descending order
"no" - otherwise
The order does not have to be strict: a sorted array can contain consecutive duplicates, e.g. [1, 1, 2, 3] is sorted in
ascending order.

It is guaranteed that there will always be a unique valid answer. More precisely:

there will be no arrays with less than 2 elements
there will be no arrays where all elements are equal
"""

def is_sorted_and_how(arr):
    is_ascending = True
    is_descending = True
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            is_descending = False
        elif arr[i] > arr[i + 1]:
            is_ascending = False
        if not is_ascending and not is_descending:
            return "no"
    if is_ascending:
        return "yes, ascending"
    elif is_descending:
        return "yes, descending"
    else:
        return "no"

# Teste

print(is_sorted_and_how([1, 2, 3, 4, 5]))     # "yes, ascending"
print(is_sorted_and_how([5, 4, 3, 2, 1]))     # "yes, descending"
print(is_sorted_and_how([1, 1, 2, 3, 4]))     # "yes, ascending"
print(is_sorted_and_how([5, 4, 4, 3, 2]))     # "yes, descending"
print(is_sorted_and_how([1, 3, 2, 4, 5]))     # "no"
print(is_sorted_and_how([2, 2, 1, 1, 0]))     # "yes, descending"