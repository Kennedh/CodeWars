"""
Dado um array não vazio de inteiros, retorna o resultado da multiplicação dos valores em ordem.
"""

def grow(arr):
    res = 1
    for n in arr:
        res *= n
    return res

# Teste

print(grow([1, 2, 3, 4]))