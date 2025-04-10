"""
O objetivo deste exercício é converter uma string em uma nova string,
onde cada caractere na nova string será "(" se esse caractere aparecer apenas uma vez na string original,
ou ")" se esse caractere aparecer mais de uma vez na string original.
Ignore o uso de maiúsculas e minúsculas ao determinar se um caractere é duplicado.
"""

def duplicate_encode(word):
    res = ""
    for l in word.lower():
        if word.lower().count(l) > 1:
            res += ")"
        else:
            res += "("
    return res

# Teste

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
print(duplicate_encode("banana"))