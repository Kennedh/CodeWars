"""
Escreva uma função que receba um inteiro como entrada e retorne o número de bits que são iguais a um na representação
binária desse número. Você pode garantir que a entrada seja não negativa.

Exemplo : A representação binária de 1234é 10011010010, então a função deve retornar 5neste caso
"""

def count_bits(n):
    return bin(n).count("1")

# Teste

print(count_bits(4))