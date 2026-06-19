"""
Complete the solution so that it reverses all of the words within the string passed in.

Words are separated by exactly one space and there are no leading or trailing spaces.
"""

def reverse_words(s):
    res = s.split()
    res.reverse()
    return " ".join(res)

# Teste

print(reverse_words("The greatest victory is that which requires no battle"))