"""
A raiz digital é a soma recursiva de todos os dígitos de um número.

Dado n, calcule a soma dos dígitos de n. Se esse valor tiver mais de um dígito, continue reduzindo dessa forma até que
um número de um dígito seja produzido. A entrada será um número inteiro não negativo.
"""

def digital_root(n):
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

# Teste

print(digital_root(132189))