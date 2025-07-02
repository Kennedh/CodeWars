"""
Como parte deste Kata, você precisa criar uma função que, quando fornecida com um tripleto, retorne o índice do elemento
numérico que fica entre os outros dois elementos.

A entrada para a função será uma matriz de três números distintos (Haskell: uma tupla).

Por exemplo:

gimme([2, 3, 1]) => 0
2 é o número que cabe entre 1 e 3 e o índice de 2 na matriz de entrada é 0 .

Outro exemplo (só para deixar claro):

gimme([5, 10, 14]) => 1
10 é o número que cabe entre 5 e 14 e o índice de 10 na matriz de entrada é 1 .
"""

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

# Teste

print(gimme([5, 10, 14]))