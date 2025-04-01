"""
Complete a função de soma quadrada para que ela eleve ao quadrado cada número passado e então some os resultados.
"""

def square_sum(numbers):
    return sum(num ** 2 for num in numbers)

# Teste

print(square_sum([0, 3, 4, 5]))