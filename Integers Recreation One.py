"""
1, 246, 2, 123, 3, 82, 6, 41são os divisores do número 246.

Elevando esses divisores ao quadrado, obtemos: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

A soma desses quadrados 84100é 290 * 290.

Tarefa
Encontre todos os números inteiros entre me n(m e n são números inteiros com 1 <= m <= n)
tais que a soma dos seus divisores quadrados seja um quadrado.

Retornaremos um array de subarrays ou de tuplas (em C um array de Pair) ou uma string.

As submatrizes (ou tuplas ou pares) terão dois elementos: primeiro o número cujos divisores ao quadrado são quadrados e,
depois, a soma dos divisores ao quadrado.
"""

import math

def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisores = [i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]
        todos_divisores = set()
        for i in divisores:
            todos_divisores.add(i)
            todos_divisores.add(num // i)
        soma_quadrados = sum(d ** 2 for d in todos_divisores)
        if math.isqrt(soma_quadrados) ** 2 == soma_quadrados:
            result.append([num, soma_quadrados])
    return result

# Teste

print(list_squared(1, 250))
print(list_squared(42, 250))