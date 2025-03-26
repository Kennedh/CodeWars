"""
Dados dois arrays a e b, escreva uma função comp(a, b) (ou compSame(a, b))
que verifica se os dois arrays têm os "mesmos" elementos, com as mesmas multiplicidades
(a multiplicidade de um membro é o número de vezes que ele aparece).
"Mesmo" significa, aqui, que os elementos em b são os elementos em a ao quadrado, independentemente da ordem.
"""

def comp(array1, array2):
    array_master = []
    for n in array1:
        array_master.append(n*n)
    return sorted(array_master)==sorted(array2)

# Teste

print(comp([121, 144, 19, 161, 19, 144, 19, 11],[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))