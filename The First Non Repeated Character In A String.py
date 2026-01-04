"""
You need to write a function, that returns the first non-repeated character in the given string.

If all the characters are unique, return the first character of the string.
If there is no unique character, return null in JS or Java, None in Python, '\0' in C.

You can assume, that the input string has always non-zero length.

Examples
"test"   returns "e"
"teeter" returns "r"
"trend"  returns "t" (all the characters are unique)
"aabbcc" returns null (all the characters are repeated)
"""

def first_non_repeated(s):
    reap = []
    non  = []
    for a in s:
        if a not in non and a not in reap:
            non.append(a)
        else:
            try:
                non.remove(a)
            except:
                pass
            reap.append(a)
    return non[0] if non else None

# Teste

print(first_non_repeated("test"))
print(first_non_repeated("teeter"))
print(first_non_repeated("trend"))
print(first_non_repeated("aabbcc"))