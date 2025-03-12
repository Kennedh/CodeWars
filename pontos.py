"""
Nosso time de futebol terminou o campeonato.

Os resultados das partidas do nosso time são registrados em uma coleção de strings. Cada partida é representada por uma string no formato "x:y", onde x é a pontuação do nosso time e y é a pontuação do nosso oponente.

Por exemplo: ["3:1", "2:2", "0:1", ...]

Os pontos são concedidos para cada partida da seguinte forma:

se x > y: 3 pontos (vitória)
se x < y: 0 pontos (derrota)
se x = y: 1 ponto (empate)
Precisamos escrever uma função que pegue essa coleção e retorne o número de pontos que nosso time (x) obteve no campeonato pelas regras fornecidas acima.

Observações:

nosso time sempre joga 10 partidas no campeonato
0 <= x <= 4
0 <= y <= 4
"""

def points(games):
    p = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            p += 3
        elif int(i[0]) == int(i[2]):
            p += 1
    return p

# Teste

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))


