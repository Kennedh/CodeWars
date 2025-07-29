"""
Escreva uma função que produza a transposta de uma matriz - uma nova matriz onde as colunas e linhas da original são
trocadas.

Por exemplo, a transposição de:

| 1 2 3 |
| 4 5 6 |
é

| 1 4 |
| 2 5 |
| 3 6 |
A entrada para sua função será um conjunto de linhas da matriz. Você pode assumir que cada linha tem o mesmo comprimento
e que a altura e a largura da matriz são positivas.
"""

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed

# Teste

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))