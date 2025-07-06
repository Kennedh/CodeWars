"""
O problema do subarray de soma máxima consiste em encontrar a soma máxima de uma subsequência contígua em um array ou
lista de inteiros:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# Deveria ser 6: [4, -1, 2, 1]

Um caso fácil é quando a lista é composta apenas por números positivos e a soma máxima é a soma de todo o array. Se a
lista for composta apenas por números negativos, retorne 0.

Uma lista vazia é considerada como tendo a maior soma nula. Observe que a lista ou matriz vazia também é uma
sublista/submatriz válida.
"""

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for n in arr:
        current_sum += n
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Teste

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))