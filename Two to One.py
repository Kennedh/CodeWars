"""
Pegue 2 strings s1, s2 incluindo apenas letras de a até z.
Retorne uma nova string ordenada (em ordem alfabética crescente),
a mais longa possível, contendo letras distintas — cada uma obtida apenas uma vez — vindas de s1 ou s2.
"""

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# Teste

print(longest("aretheyhere", "yestheyarehere"))