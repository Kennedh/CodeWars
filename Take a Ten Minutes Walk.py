"""
Você mora na cidade de Cartesia, onde todas as ruas são dispostas em uma grade perfeita.
Você chegou dez minutos mais cedo para um compromisso,
então decidiu aproveitar a oportunidade para dar uma curta caminhada.
A cidade fornece aos seus cidadãos um aplicativo gerador de caminhadas em seus celulares —
toda vez que você pressiona o botão,
ele envia uma matriz de strings de uma letra representando as direções para caminhar (por exemplo, ['n', 's', 'w', 'e']).
Você sempre anda apenas um único quarteirão para cada letra (direção) e
sabe que leva um minuto para atravessar um quarteirão da cidade,
então crie uma função que retorne true se a caminhada
que o aplicativo fornece levar exatamente dez minutos (você não quer chegar cedo ou atrasado!) e, claro,
retornará você ao seu ponto de partida.
Retorne false caso contrário.
"""

def is_valid_walk(walk):
    cordinates = [0,0]
    for d in walk:
        if d == "n":
            cordinates[0] += 1
        elif d == "s":
            cordinates[0] -= 1
        if d == "e":
            cordinates[1] += 1
        elif d == "w":
            cordinates[1] -= 1
    if len(walk) == 10 and cordinates == [0, 0]:
        return True
    else:
        return False

# Teste

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
