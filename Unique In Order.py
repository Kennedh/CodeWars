"""
Implemente a função unique_in_order que recebe como argumento uma sequência e
retorna uma lista de itens sem nenhum elemento com o mesmo valor um ao lado do outro e
preservando a ordem original dos elementos.
"""

def unique_in_order(sequence):
    res = []
    for l in sequence:
        if not res:
            res.append(l)
        if res[-1] != l:
            res.append(l)
    return res

# Teste

print(unique_in_order('AAAABBBCCDAABBB'))