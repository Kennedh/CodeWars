"""
Retorna o número (contagem) de vogais na string fornecida.

Consideraremos a, e, i, o, u como vogais para este Kata (mas não y).

A string de entrada consistirá apenas de letras minúsculas e/ou espaços.
"""

def get_count(w):
    vowels = "aeiou"
    return sum(1 for l in w if l in vowels)

#Example

print(get_count("word"))
