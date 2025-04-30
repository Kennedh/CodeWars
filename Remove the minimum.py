"""
Dado um array de inteiros, remova o menor valor.
Não altere o array/lista original. Se houver vários elementos com o mesmo valor, remova aquele com o menor índice.
Se você obtiver um array/lista vazio, retorne um array/lista vazio.

Não altere a ordem dos elementos restantes.
"""

def remove_smallest(numbers):
    res = [num for num in numbers]
    if res:
        res.remove(min(res))
    return res

# Teste

print(remove_smallest([1, 2, 3, 1, 1]))