"""
São dados dois ângulos internos (em graus) de um triângulo.

Escreva uma função para retornar o 3º.

Observação: somente números inteiros positivos serão testados.
"""

def other_angle(a, b):
    return 180 - (a + b)

# Teste

print(other_angle(30, 60))