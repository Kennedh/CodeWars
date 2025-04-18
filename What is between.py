"""
Complete a função que recebe dois inteiros ( a, b, onde a < b)
e retorna uma matriz de todos os inteiros entre os parâmetros de entrada, incluindo eles.
"""

def between(a,b):
    res = []
    while a <= b:
        res.append(a)
        a += 1
    return res

# Teste

print(between(1,4))
print(between(-2,4))