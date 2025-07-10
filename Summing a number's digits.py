"""
Escreva uma função que receba um número como entrada e retorne a soma do valor absoluto de cada um dos
dígitos decimais do número.
"""

def sum_digits(number):
    res = 0
    for num in str(number):
        if num.isdigit():
            res += int(num)
    return res

# Teste

print(sum_digits(312123))