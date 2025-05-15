"""
Neste exercício simples, você escreverá uma função que recebe dois inteiros; ne limit;
e retorna uma lista de múltiplos de naté e possivelmente incluindo limit.

É garantido que n > 0e limit >= n.

Por exemplo, se os parâmetros passados forem (2, 6),
a função deve retornar [2, 4, 6]como 2, 4, e 6 são múltiplos de 2até 6.
"""

def find_multiples(integer, limit):
    return [n for n in range(integer,limit+1,integer)]

# Teste

print(find_multiples(5, 25))
print(find_multiples(1, 2))