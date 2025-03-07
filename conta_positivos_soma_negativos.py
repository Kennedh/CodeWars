"""Dado um array de inteiros.

Retorna um array, onde o primeiro elemento é a contagem de números positivos e
o segundo elemento é a soma de números negativos. 0 não é positivo nem negativo.

Se a entrada for um array vazio ou for nulo, retorna um array vazio."""

def count_positives_sum_negatives(arr):
    cp = 0
    result = []
    sn = 0
    for n in arr:
        if n > 0:
            cp += 1
        elif n < 0:
            sn += n
    result.append(cp)
    result.append(sn)
    if arr == []:
        result = []
    return result

# Teste

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0,0]))
print(count_positives_sum_negatives([]))