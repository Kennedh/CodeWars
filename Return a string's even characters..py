"""
Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string
is smaller than two characters or longer than 100 characters, the function should return "invalid string".

For example:

"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
"""

def even_chars(st):
    if len(st) <= 1 or len(st) > 100:
        return "invalid string"
    return [a for idx, a in enumerate(st) if idx % 2 != 0]

# Teste

print(even_chars("abcdefghijklm"))
print(even_chars("a"))