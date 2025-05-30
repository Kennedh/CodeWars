"""
Você receberá um array de números inteiros. Sua tarefa é pegar esse array e encontrar um índice N onde a soma
dos números inteiros à esquerda de N seja igual à soma dos números inteiros à direita de N.

Se não houver nenhum índice que faça isso acontecer, retorne -1.

Por exemplo:
Digamos que você recebeu o array {1,2,3,4,3,2,1}:
Sua função retornará o índice 3, porque na 3ª posição do array, a soma do lado esquerdo do índice ( {1,2,3})
e a soma do lado direito do índice ( {3,2,1}) são iguais 6.

Vejamos outro exemplo.
Você recebe o array {1,100,50,-51,1,1}:
Sua função retornará o índice 1, porque na primeira posição do array, a soma do lado esquerdo do índice ( {1})
e a soma do lado direito do índice ( {50,-51,1,1}) são iguais 1.

Último:
Você recebe o array {20,10,-80,10,10,15,35}
No índice 0 o lado esquerdo é {}
O lado direito é {10,-80,10,10,15,35}
Ambos são iguais a 0quando adicionados. (Matrizes vazias são iguais a 0 neste problema)
O índice 0 é o lugar onde o lado esquerdo e o lado direito são iguais.

Nota: Lembre-se de que na maioria das linguagens o índice de uma matriz começa em 0.
"""

def find_even_index(arr):
    for idx ,num in enumerate(arr):
        if sum(arr[:idx]) == sum(arr[idx+1:]):
            return idx
    return -1

# Teste

print(find_even_index([1,2,3,4,3,2,1]))