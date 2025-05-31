"""
Crie uma função de combate que considere a saúde atual do jogador e
a quantidade de dano recebido e retorne a nova saúde do jogador. A saúde não pode ser menor que 0 .
"""

def combat(health, damage):
    return health - damage if health - damage >= 0 else 0

# Teste

print(combat(100, 5))
print(combat(10, 20))