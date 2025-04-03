"""
Dado um inteiro não negativo, 3 por exemplo, retorne uma string com um murmúrio: "1 ovelha...2 ovelhas...3 ovelhas...".
A entrada sempre será válida, ou seja, nenhum inteiro negativo.
"""

def count_sheep(n):
    count = ""
    for sheep in range(n):
        count += f"{sheep + 1} sheep..."
    return count


# Teste

print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))
print(count_sheep(4))
