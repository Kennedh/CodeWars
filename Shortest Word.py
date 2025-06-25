"""
Dada uma sequência de palavras, retorne o comprimento da(s) palavra(s) mais curta(s).

A string nunca estará vazia e você não precisa levar em conta diferentes tipos de dados.
"""



def find_short(s):
    s = s.split(" ")
    s = sorted(s, key = len)
    return len(s[0])

# Teste

print(find_short("bitcoin take over the world maybe who knows perhaps"))

