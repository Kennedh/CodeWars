"""
Dada uma lista e um número, crie uma nova lista que contenha cada número da lista no máximo N vezes, sem reordenar.
Por exemplo, se o número de entrada for 2, e a lista de entrada for [1,2,3,1,2,1,2,3], você pega [1,2,3,1,2],
descarta o próximo [1,2], pois isso levaria a 1 e 2 estarem no resultado 3 vezes, e então pega 3,
o que leva a [1,2,3,1,2,3]. Com a lista [20,37,20,21] e o número 1, o resultado seria [20,37,21].
"""


def delete_nth(order, max_e):
    counts = {}
    result = []

    for num in order:
        if counts.get(num, 0) < max_e:
            result.append(num)
            counts[num] = counts.get(num, 0) + 1

    return result


# Teste

print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
print(delete_nth([20, 37, 20, 21], 1))