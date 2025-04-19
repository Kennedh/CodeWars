"""
Dada uma sequência de palavras, você precisa encontrar a palavra com maior pontuação.

Cada letra de uma palavra marca pontos de acordo com sua posição no alfabeto: a = 1, b = 2, c = 3etc.

Por exemplo, a pontuação de abadé 8(1 + 2 + 1 + 4).

Você precisa retornar a palavra com maior pontuação como uma string.

Se duas palavras tiverem a mesma pontuação, retorne a palavra que aparecer primeiro na string original.

Todas as letras serão minúsculas e todas as entradas serão válidas.
"""

def alf_num(l):
    return ord(l.lower()) - ord("a") + 1

def high(x):
    word = ""
    num = 0
    for w in x.split():
        if sum(alf_num(l) for l in w) > num:
            word = w
            num = sum(alf_num(l) for l in w)
    return word

# Teste

print(high('man i need a taxi up to ubud'))