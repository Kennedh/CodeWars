"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging
 digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""

def next_bigger(n):
    n = list(str(n))
    temp = []
    for i in range(len(n) - 2, -1, -1):
        if n[i] < n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            if len(n[i + 1:]) > 0:
                temp = n[i + 1:]
                del n[i + 1:]
                n.insert(-1,sorted(temp))
                return n
    return -1

# Teste

print(next_bigger(12))