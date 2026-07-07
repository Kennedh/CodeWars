"""
When provided with a letter, return its position in the alphabet.

Input :: "a"

Output :: "Position of alphabet: 1"

Note: Only lowercased English letters are tested
"""

def position(letter):
    return f"Position of alphabet: {ord(letter) - 96}"

# Teste

print(position("a"))
print(position("z"))
print(position("e"))