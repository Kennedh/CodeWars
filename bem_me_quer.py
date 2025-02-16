"""
Timmy e Sarah acham que estão apaixonados, mas perto de onde moram, eles só saberão quando colherem uma flor cada.
Se uma das flores tiver um número par de pétalas e a outra tiver um número ímpar de pétalas,
significa que eles estão apaixonados.

Escreva uma função que pegue o número de pétalas de cada flor
e retorne true se elas estiverem apaixonadas e false se não estiverem.
"""
from site import abs_paths


def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower2 % 2 == 0 and flower1 % 2 != 0):
        apaixonados = True
    else:
        apaixonados = False
    return apaixonados

# Teste

n1 = 3
n2 = 5

print(lovefunc(n1,n2))
