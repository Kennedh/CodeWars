"""
Você consegue encontrar a agulha no palheiro?

Escreva uma função findNeedle()que receba um arraymonte de lixo, mas que contenha um"needle"

Depois que sua função encontrar a agulha, ela deverá retornar uma mensagem (como uma string) que diz:

"found the needle at position "mais indexele encontrou a agulha, então:
"""

def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

# Teste

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))