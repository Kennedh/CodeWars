"""
Implemente uma função que calcule a diferença entre duas listas.
A função deve remover todas as ocorrências de elementos da primeira lista (a) que estão presentes na segunda lista (b).
A ordem dos elementos na primeira lista deve ser preservada no resultado.
"""

def array_diff(a, b):
    diff = []
    for string in a:
        if string not in b:
            diff.append(string)
    return diff

# Teste

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))