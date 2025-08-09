"""Se todo o array for consecutivo, então retorne null2 .

A matriz sempre terá pelo menos 2o elemento 1 e todos os elementos serão números. Os números também serão únicos e
estarão em ordem crescente. Os números podem ser positivos ou negativos, e o primeiro não consecutivo também pode ser
qualquer um!

1 Você consegue escrever uma solução que retorne null2 para ambos []e [ x ]? (Este é um array vazio com um único número
e não foi testado, mas você pode escrever seu próprio teste de exemplo.)"""

def first_non_consecutive(arr):
    if not arr and len(arr) <= 1:
        return None
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1:
            return arr[i]

# Teste

print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))