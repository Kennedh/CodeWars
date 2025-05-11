"""
Mary tem outro livro de quebra-cabeças, e cabe a você ajudá-la! Este livro está cheio de substrings terminadas em zero,
e você precisa encontrar a substring com a maior soma de seus dígitos. Por exemplo, um quebra-cabeça se parece com este:

"72102450111111090"
Aqui, existem 4 substrings diferentes: 721, 245, 111111, e 9. As somas de seus dígitos são 10, 11, 6, e 9, respectivamente.
Portanto, a substring com a maior soma de seus dígitos é 245, e sua soma é 11.

Escreva uma função largest_sumque receba uma string e retorne o máximo das somas das substrings.
No exemplo acima, sua função deve retornar 11.
"""

def largest_sum(s):
    parts = s.split('0')
    max_sum = 0
    for part in parts:
        current_sum = sum(int(c) for c in part)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Teste

print(largest_sum("72102450111111090"))