"""
Encontre a soma de todos os múltiplos nabaixom

Ter em mente
n e m são números naturais (inteiros positivos)
m é excluído dos múltiplos
"""


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    total = 0
    for i in range(n, m, n):
        total += i
    return total

# Teste

print(sum_mul(0, 0))
print(sum_mul(2, 9))
print(sum_mul(4, 123))