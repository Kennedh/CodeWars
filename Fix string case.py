"""
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to
convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!
"""

def solve(s):
    low = 0
    up  = 0
    for l in s:
        if l.islower():
            low += 1
        else:
            up += 1
    if low >= up:
        return s.lower()
    else:
        return s.upper()

# Teste

print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))
