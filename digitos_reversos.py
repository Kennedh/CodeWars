"""
Dado um número aleatório não negativo, você deve retornar os dígitos desse número dentro de uma matriz na ordem inversa.
"""

def digitize(n):
    return [int(d) for d in str(n)[::-1]]

# Teste

print(digitize(35231))