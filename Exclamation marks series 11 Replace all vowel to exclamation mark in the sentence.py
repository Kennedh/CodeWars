"""
Substitua todas as vogais por pontos de exclamação na frase. aeiouAEIOUé vogal.
"""

def replace_exclamation(st):
    res = ""
    for l in st:
        if l in "aeiouAEIOU":
            res += "!"
        else:
            res += l
    return res

# Teste

print(replace_exclamation("Hi!"))