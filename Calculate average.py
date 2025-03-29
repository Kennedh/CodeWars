"""
Escreva uma função que calcule a média dos números em uma determinada matriz.
"""

def find_average(numbers):
    if sum(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

# Teste

print(find_average([1, 2, 3]))
print(find_average([]))