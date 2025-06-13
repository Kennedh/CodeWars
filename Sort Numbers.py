"""Conclua a solução para que ela classifique o array de números passado.
Se a função passar um array vazio ou um valor nulo/nulo, ela deverá retornar um array vazio."""

def solution(nums):
    if not nums:
        return []
    else:
        return sorted(nums)

# Teste

print(solution([6,9,2,6,9]))