"""
Dados dois números inteiros ae b, que podem ser positivos ou negativos,
encontre a soma de todos os números inteiros entre eles e incluindo-os e retorne-a.
Se os dois números forem iguais, retorne aou b.

Nota: a e bnão são ordenados!
"""

def get_sum(a,b):
    res = 0
    if a < b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    for num in range(num1, num2+1):
        res += num
    return res

# Teste

print(get_sum(0,1))