"""
Escreva uma função que receba um array de strings como argumento e retorne um array ordenado contendo as mesmas strings,
ordenadas do menor para o maior.

Por exemplo, se esta matriz fosse passada como argumento:

["Telescopes", "Glasses", "Eyes", "Monocles"]
Sua função retornaria o seguinte array:

["Eyes", "Glasses", "Monocles", "Telescopes"]
Todas as strings no array passado para sua função terão comprimentos diferentes, então você não precisará decidir como
ordenar várias strings do mesmo comprimento.


"""

def sort_by_length(arr):
    arr.sort(key=len)
    return arr

# Teste

print(sort_by_length(["a short sentence", "a longer sentence", "the longest sentence"]))