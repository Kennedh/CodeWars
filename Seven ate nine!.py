"""
Seven is a hungry number and its favourite food is number 9. Whenever it spots 9 through the hoops of 8, it eats it!
Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of
digits and tell 7 to come after 9 instead. Seven "ate" nine, no more! (If 9 is not in danger, just return the same
array)
"""

def hungry_seven(arr):
    res = arr[:]
    i = 0
    while i < len(res) - 2:
        if res[i] == 7 and res[i + 1] == 8 and res[i + 2] == 9:
            res[i + 1], res[i + 2] = res[i + 2], res[i + 1]
            i += 3
        else:
            i += 1
    return res

# Teste

print(hungry_seven([7,8,9]))
print(hungry_seven([7,7,7,8,9]))
print(hungry_seven([8,7,8,9,8,9,7,8]))
print(hungry_seven([8,7,8,7,9,8]))