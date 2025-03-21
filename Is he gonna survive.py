"""
Um herói está a caminho do castelo para completar sua missão.
No entanto, ele foi informado de que o castelo está cercado por dois dragões poderosos!
Cada dragão leva 2 balas para ser derrotado, nosso herói não tem ideia de quantas balas ele deve carregar.
Supondo que ele vá pegar um número específico de balas e
seguir em frente para lutar contra outro número específico de dragões, ele sobreviverá?

Retorne true se sim, false caso contrário :)
"""

def hero(bullets, dragons):
    return (dragons * 2) <= bullets

# Teste

print(hero(10, 5))
print(hero(7, 4))
print(hero(4, 5))
print(hero(100, 40))
print(hero(1500, 751))
print(hero(0, 1))