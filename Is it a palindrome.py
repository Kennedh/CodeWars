"""
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards,

such as madam or racecar.
"""

def is_palindrome(s):
    s = s.lower()
    return True if s == s[::-1] else False

# Teste

print(is_palindrome('malam'))
print(is_palindrome('walter'))
print(is_palindrome('kodok'))