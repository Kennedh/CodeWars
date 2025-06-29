"""
Esta função deve testar se o factoré um fator de base.

Retorne truese é um fator ou falsenão.

Sobre fatores
Fatores são números que você pode multiplicar para obter outro número.

2 e 3 são fatores de 6 porque:2 * 3 = 6

Você pode encontrar um fator dividindo números. Se o resto for 0, o número é um fator.
Você pode usar o operador mod ( %) na maioria dos idiomas para verificar se há um resto
Por exemplo, 2 não é um fator de 7 porque:7 % 2 = 1

Nota: baseé um número não negativo, factoré um número positivo.
"""

def check_for_factor(base, factor):
    return base % factor == 0

# Teste

print(check_for_factor(4,2))
print(check_for_factor(80,3))
