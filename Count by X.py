"""
Crie uma função com dois argumentos que retornará uma matriz dos primeiros nmúltiplos de x.

Suponha que tanto o número fornecido quanto o número de vezes a serem contados serão números positivos maiores que 0.

Retorna os resultados como uma matriz ou lista (dependendo do idioma).
"""

def count_by(x, n):
    seq = []
    i = 0
    num = 0
    while i < n:
        i += 1
        num += x
        seq.append(num)
    return seq

# Teste

print(count_by(2,5))