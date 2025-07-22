"""
Boliche de dez pinos
No boliche de dez pinos, um jogador rola uma bola de boliche por uma pista para derrubar os pinos. Há dez pinos
dispostos no final da pista. Cada jogador tem 10 jogadas para rolar uma bola de boliche por uma pista e derrubar o
máximo de pinos possível. As primeiras nove jogadas terminam após dois lançamentos ou quando o jogador derruba todos os
pinos. Na última jogada, o jogador receberá uma jogada extra cada vez que derrubar todos os dez pinos; até um máximo de
três lançamentos no total.

O Desafio
Neste desafio, você receberá uma string representando os dez frames de um jogador. Ela será mais ou menos assim:
'X X 9/ 80 X X 90 8/ 7/ 44'(em Java: "X X 9/ 80 X X 90 8/ 7/ 44"), onde cada frame é delimitado por espaços,
'X'representa strikes e '/'spares. Seu objetivo é inserir essa string de frames em uma função chamada bowlingScoree
retornar a pontuação total do jogador.
"""

def bowling_score(frames):
    rolls = []
    total = 0
    for frame in frames.split():
        for p in frame:
            if p == "X":
                rolls.append(10)
            elif p == "/":
                rolls.append(10 - int(rolls[-1]))
            else:
                rolls.append(int(p))
    roll_idx = 0
    for n in range(10):
        if rolls[roll_idx] == 10:
            total += rolls[roll_idx] + rolls[roll_idx + 1] + rolls[roll_idx + 2]
            roll_idx += 1
        elif rolls[roll_idx] + rolls[roll_idx + 1] == 10:
            total += rolls[roll_idx] + rolls[roll_idx + 1] + rolls[roll_idx + 2]
            roll_idx += 2
        else:
            total += rolls[roll_idx] + rolls[roll_idx + 1]
            roll_idx += 2
    return total

# Teste

print(bowling_score('71 43 80 8/ 45 9/ 06 2/ 81 53')) # 97
print(bowling_score('8/ 41 71 70 54 63 35 33 06 12')) # 75
print(bowling_score("71 04 72 32 25 42 45 9/ 43 XX1")) # 90
