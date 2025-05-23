"""
Há uma fila para os caixas de autoatendimento do supermercado.
Sua tarefa é escrever uma função para calcular o tempo total necessário para todos os clientes finalizarem a compra!

entrada
clientes: um conjunto de números inteiros positivos representando a fila.
Cada número inteiro representa um cliente, e seu valor é o tempo que ele leva para finalizar a compra.
n: um número inteiro positivo, o número de caixas registradoras.
saída
A função deve retornar um inteiro, o tempo total necessário.
"""

def queue_time(customers, n):
    if not customers:
        return 0
    tills = [0] * n
    for customer in customers:
        idx = tills.index(min(tills))
        tills[idx] += customer
    return max(tills)

# teste

print(queue_time([5, 3, 4], 1))