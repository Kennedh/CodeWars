"""
Construa uma torre em forma de pirâmide, como uma matriz/lista de strings, dado um número inteiro positivo de andares.
Um bloco de torres é representado pelo caractere "*".
"""

def tower_builder(n_floors):
    res = []
    n = 0
    t = 1
    spaces = n_floors

    while n_floors > n:
        res.append(" " * (spaces - 1) + "*" * t + " " * (spaces - 1))
        n += 1
        t += 2
        spaces -= 1

    return res

# Teste

print(tower_builder(5))
print(tower_builder(7))
print(tower_builder(9))

