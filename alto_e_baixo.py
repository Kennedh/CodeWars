"""
Nesta pequena tarefa, você recebe uma sequência de números separados por espaços e deve retornar o maior e o menor número.
"""

def high_and_low(numbers):
    return f"{max(map(int, numbers.split(' ')))} {min(map(int, numbers.split(' ')))}"

# Teste

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


