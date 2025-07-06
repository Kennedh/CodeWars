"""
Muito simples, dado um número (inteiro / decimal / ambos, dependendo do idioma), encontre seu oposto (inverso aditivo).
"""

def opposite(number):
    number -= number + number
    return number

# Teste

print(opposite(-1))
print(opposite(3))
print(opposite(-622))
print(opposite(0))