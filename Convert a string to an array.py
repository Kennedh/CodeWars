"""
Write a function to split a string and convert it into an array of words.
"""

def string_to_array(s):
    return s.split() if s else ['']

# Teste

print(string_to_array("I love arrays they are my favorite"))