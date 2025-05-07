"""
Dado um conjunto X de inteiros positivos, seus elementos devem ser transformados
executando a seguinte operação neles quantas vezes forem necessárias:

if X[i] > X[j] then X[i] = X[i] - X[j]

Quando não forem possíveis mais transformações, retorne sua soma ("menor soma possível").
"""

def solution(lst):
    while len(set(lst)) > 1:
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i] > lst[j]:
                    lst[i] = lst[i] - lst[j]
    return sum(lst)

# Teste

print(solution ([6, 9, 21]))