"""
Implemente uma função que some dois números e retorne sua soma em binário. A conversão pode ser feita antes ou depois da adição.

O número binário retornado deve ser uma string.
"""

def add_binary(a,b):
    add = a + b
    return bin(add)[2:]

print(add_binary(1,1))

