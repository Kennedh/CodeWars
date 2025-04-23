"""
Dado um conjunto de números inteiros, encontre aquele que aparece um número ímpar de vezes.

Sempre haverá apenas um número inteiro que aparece um número ímpar de vezes.
"""

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

# Teste

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))