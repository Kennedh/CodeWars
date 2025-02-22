"""
Crie uma função que receba um inteiro como argumento e retorne "Par" para números pares ou "Ímpar" para números ímpares.
"""

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Teste

print(even_or_odd(2))
print(even_or_odd(3))