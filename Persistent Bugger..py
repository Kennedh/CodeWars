"""
Escreva uma função, persistence, que recebe um parâmetro positivo "num" e retorna sua persistência multiplicativa,
que é o número de vezes que você deve multiplicar os dígitos "num" até chegar a um único dígito.
"""

def persistence(n):
    res = 0
    while n >= 10:
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        n = prod
        res += 1
    return res

# Teste

print(persistence(999))