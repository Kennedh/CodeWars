"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below.
Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
"""

def capitalize(s):
    a = "".join([a.upper() if idx % 2 == 0 else a.lower() for idx, a in enumerate(s)])
    b = "".join([a.upper() if idx % 2 != 0 else a.lower() for idx, a in enumerate(s)])
    return [a, b]

# Teste

print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("abracadabra"))
print(capitalize("indexinglessons"))