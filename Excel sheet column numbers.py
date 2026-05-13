"""
Write a function that, given a column title as it appears in an Excel sheet, returns its corresponding column number.

All column titles will be uppercase.

Examples:

Column title: "A" --> return 1
Column title: "Z" --> return 26
Column title: "AA" --> return 27

"""


def title_to_number(title: str) -> int:
    return sum((ord(char) - ord('A') + 1) * (26 ** i) 
               for i, char in enumerate(reversed(title)))

# Teste

print(title_to_number("A"))
print(title_to_number("Z"))
print(title_to_number("AA"))
