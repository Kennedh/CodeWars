"""
Dado um array bidimensional de inteiros, retorne a versão achatada do array com todos os inteiros em ordem crescente.

Exemplo:

Dado [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], sua função deve retornar [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""

def flatten_and_sort(array):
    res = []
    for x in array:
        for y in x:
            res.append(y)
    return sorted(res)

# Teste

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))