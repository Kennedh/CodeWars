"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word
upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there
are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""

def to_weird_case(words):
    lista = words.split()
    for i in range(len(lista)):
        temp = list(lista[i])
        for j in range(len(temp)):
            if j % 2 == 0:
                temp[j] = temp[j].upper()
            else:
                temp[j] = temp[j].lower()
        lista[i] = "".join(temp)
    return " ".join(lista)

# Teste

print(to_weird_case("THIs iS a TEST"))
