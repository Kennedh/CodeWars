"""
Você receberá um array ae um valor x. Tudo o que você precisa fazer é verificar se o array fornecido contém o valor.

apode conter números ou strings. xpode ser qualquer um.

Retorna truese o array contém o valor, falsecaso contrário.
"""

def check(seq, elem):
    return elem in seq

# Teste

print(check([66, 101], 66))