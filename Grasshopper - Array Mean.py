"""
Encontre a média
Encontre a média de uma lista de números em uma matriz.

Informação
Para encontrar a média de um conjunto de números, some todos os números e divida pelo número de valores na lista.
"""

def find_average(nums):
    return sum(nums) / len(nums)

# Teste

print(find_average([-1, 3, 5, -7]))