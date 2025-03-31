"""
Dado um array de inteiros como strings e números, retorne a soma dos valores do array como se todos fossem números.

Retorne sua resposta como um número.
"""

def sum_mix(arr):
    res = 0
    for num in arr:
        res += int(num)
    return res

# Teste

print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))