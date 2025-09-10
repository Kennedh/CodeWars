"""
O objetivo do Pato, pato, ganso é andar em círculo , tocando na cabeça de cada jogador até que um seja escolhido.

Tarefa:

Dado um conjunto de objetos Player e uma posição (a primeira posição é 1), retorne o namedo Player escolhido.
nameé uma propriedade de Playerobjetos, por exemploPlayer.name

Exemplo:

duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name
"""

def duck_duck_goose(players, goose):
    index = (goose - 1) % len(players)
    return players[index].name

# Teste

class Player:
    def __init__(self, name):
        self.name = name

players = [Player("Ana"), Player("Bruno"), Player("Carlos")]
print(duck_duck_goose(players, 5))