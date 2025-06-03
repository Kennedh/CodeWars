"""
Dado um conjunto de uns e zeros, converta o valor binário equivalente em um inteiro.

Ex: [0, 0, 0, 1]é tratado como 0001que é a representação binária de 1.
"""

def binary_array_to_number(arr):
    return int("".join(str(n) for n in arr), 2)

# Teste

print(binary_array_to_number([1, 1, 1, 0]))