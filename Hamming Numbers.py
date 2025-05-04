"""
Um número de Hamming é um inteiro positivo da forma 2 i 3 j 5 k , para alguns inteiros não negativos i, j e k.

Escreva uma função que calcule o n -ésimo menor número de Hamming.

Especificamente:

O primeiro menor número de Hamming é 1 = 2 0 3 0 5 0
O segundo menor número de Hamming é 2 = 2 1 3 0 5 0
O terceiro menor número de Hamming é 3 = 2 0 3 1 5 0
O quarto menor número de Hamming é 4 = 2 2 3 0 5 0
O quinto menor número de Hamming é 5 = 2 0 3 0 5 1
"""

import heapq


def hamming(n):
    heap = [1]
    seen = set([1])
    primes = [2, 3, 5]

    for _ in range(n):
        current = heapq.heappop(heap)
        for p in primes:
            new_val = current * p
            if new_val not in seen:
                seen.add(new_val)
                heapq.heappush(heap, new_val)
    return current

# Teste

print(hamming(15))