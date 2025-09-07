"""
Dado um conjunto de números, retorne o inverso aditivo de cada um. Cada positivo se torna negativo, e os negativos se
tornam positivos.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
Você pode assumir que todos os valores são inteiros. Não altere a matriz de entrada.
"""

def invert(lst):
    if not lst:
        return []
    else:
        return [n * -1 for n in lst]

# Teste

print(invert([1, -2, 3, -4, 5]))
print(invert([]))