"""
Complete a função que recebe 3 números x, y and k(onde x ≤ y) e retorna o número de inteiros dentro do intervalo [x..y]
(ambas as extremidades incluídas) que são divisíveis por k.

Mais cientificamente: { i : x ≤ i ≤ y, i mod k = 0 }

Exemplo
Dado que x = 6, y = 11, k = 2a função deve retornar 3, porque há três números divisíveis por 2entre 6e 11:6, 8, 10

Observação : os casos de teste são muito grandes. Você precisará de uma solução O(log n) ou melhor para passar.
(Uma solução de tempo constante é possível.)

"""

def divisible_count(x, y, k):
    count_y = y // k
    count_x_minus_1 = (x - 1) // k

    return count_y - count_x_minus_1

# Teste

print(divisible_count(6,11,2))