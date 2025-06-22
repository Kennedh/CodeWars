"""
Os americanos são pessoas estranhas: em seus prédios, o primeiro andar é, na verdade,
o térreo e não há 13º andar (devido à superstição).

Escreva uma função que, dado um piso no sistema americano, retorne o piso no sistema europeu.

Com a substituição do 1º andar pelo térreo e a remoção do 13º andar, os números descem para ocupar seus lugares.
Acima de 13, eles descem dois números, pois há dois números omitidos abaixo deles.

Os porões (negativos) permanecem os mesmos do nível universal.

Mais informações aqui
"""

def get_real_floor(n):
    return n - 2 if n > 13 else (n if n < 1 else n - 1)

# Teste

print(get_real_floor(15))
print(get_real_floor(5))
print(get_real_floor(1))
print(get_real_floor(0))
print(get_real_floor(-5))