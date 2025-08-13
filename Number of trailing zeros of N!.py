"""
Escreva um programa que calcule o número de zeros à direita em um fatorial de um número dado.

N! = 1 * 2 * 3 *  ... * N
"""

def zeros(n):
    total = 0
    p = 5
    while n // p > 0:
        total += n // p
        p *= 5
    return total

# Teste

print(zeros(12))