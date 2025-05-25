"""
Sua tarefa é criar uma tabela de multiplicação N×N, do tamanho fornecido no parâmetro.

Por exemplo, quando dado sizeé 3:

1 2 3
2 4 6
3 6 9
Para o exemplo fornecido, o valor de retorno deve ser:

[[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    temp = []
    res = []
    for n in range(1, size+1):
        for p in range(1, size+1):
            temp.append(p * n)
        res.append(temp)
        temp = []
    return res

# Teste

print(multiplication_table(5))
