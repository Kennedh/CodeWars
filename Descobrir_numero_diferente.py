"""
Você recebe um array (que terá um comprimento de pelo menos 3, mas pode ser muito grande) contendo inteiros.
O array é composto inteiramente de inteiros ímpares ou composto inteiramente de inteiros pares,
exceto por um único inteiro.
Escreva um metodo que receba o array como argumento e retorne esse outlier N.
"""

def num_dif(i):
    count_p = sum(1 for n in i [:3] if n % 2 == 0) #Vai verificar se os três primeiros números são par
    m_p = count_p >= 2 #Define se a maior parte é par

    for n in i: #Irá percorrer a lista para identificar um número fora do padrão
        if (n % 2 == 0) != m_p:
            return n #Irá retornar o número que é diferente dos demais

#Example

print(num_dif([1,3,5,7,8,9]))
print(num_dif([2,4,6,8,9,10]))