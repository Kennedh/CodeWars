"""
Aqui está uma maneira de construir uma lista contendo todos os números racionais positivos:

Crie uma árvore binária onde cada nó é um racional e a raiz é 1/1, com as seguintes regras para criar os nós abaixo:

O valor do nó esquerdo abaixo a/béa/a+b
O valor do nó direito abaixo a/béa+b/b
Então a árvore ficará assim:

                       1/1
                  /           \
            1/2                  2/1
           /    \              /     \
       1/3        3/2        2/3       3/1
      /   \      /   \      /   \     /   \
   1/4    4/3  3/5   5/2  2/5   5/3  3/4   4/1

 ...
Agora percorra a árvore, começando pela largura, para obter uma lista de racionais.

[ 1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, 1/4, 4/3, 3/5, 5/2, .. ]
Todo racional positivo ocorrerá, em sua forma reduzida, exatamente uma vez na lista, em um índice finito.

Usando este método você pode criar uma lista infinita de tuplas:

allRationals :: [(Integer, Integer)]
correspondendo à lista descrita acima:

allRationals = [(1,1), (1,2), (2,1), (1,3), (3,2), ...]
No entanto, construir a lista em si é muito lento para os nossos propósitos. Em vez disso, estude a árvore acima e
escreva duas funções:

-- return the value at the given index
ratAt :: Integer -> (Integer, Integer)

-- return the index of the given rational
indexOf :: (Integer, Integer) -> Integer
Por exemplo:

ratAt 10 = (5, 2)
indexOf (3,5) = 9
"""

def rat_at(n):
    k = n + 1
    b = bin(k)[2:]
    path = b[1:]
    (a, b) = (1, 1)
    for c in str(path):
        if c == "0":
            (a, b) = (a, a + b)
        elif c == "1":
            (a, b) = (a + b, b)
    return (a, b)

def index_of(a, b):
    res = ""
    while (a, b) != (1, 1):
        if a > b:
            a, b = a - b, b
            res += "1"
        elif b > a:
            a, b = a, b - a
            res += "0"
    res = res[::-1]
    res = "1" + res
    k = int(res, 2)
    n = k -1
    return n


# Teste

print(rat_at(4))
print(index_of(3, 2))













