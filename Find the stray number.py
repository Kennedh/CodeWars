"""
Você recebe uma matriz de números inteiros de comprimento ímpar , em que todos eles são iguais, exceto por um único
número.

Complete o método que aceita tal matriz e retorna aquele único número diferente.

A matriz de entrada sempre será válida! (comprimento ímpar >= 3)
"""

def stray(arr):
    num1 = [0,0]
    num2 = [0,0]
    num1[0] = arr[0]
    for n in arr:
        if n == num1[0]:
            num1[1] += 1
        else:
            num2[0] = n
            num2[1] += 1
    return num1[0] if num1[1] < num2[1] else num2[0]

# Teste

print(stray([1, 1, 1, 1, 1, 1, 2]))