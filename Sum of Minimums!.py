"""
Dada uma lista 2D (aninhada) (matriz, vetor, ..) de tamanho m * n,
sua tarefa é encontrar a soma dos valores mínimos em cada linha.
"""

def sum_of_minimums(numbers):
    return sum([min(li) for li in numbers])

# Teste

print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))