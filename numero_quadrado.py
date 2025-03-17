"""
Tarefa
Dado um número integral, determine se é um número quadrado:

Em matemática, um número quadrado ou quadrado perfeito é um inteiro que é o quadrado de um inteiro; em outras palavras,
é o produto de algum inteiro consigo mesmo.

Os testes sempre usarão algum número integral, então não se preocupe com isso em linguagens de tipagem dinâmica.
"""

def is_square(n):
    if n < 0:
        return False
    return (n ** 0.5).is_integer()

# Teste

print(is_square(16))
print(is_square(25))
print(is_square(26))
print(is_square(1))
print(is_square(0))