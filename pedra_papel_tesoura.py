"""
Pedra, Papel, Tesoura

Você tem que retornar qual jogador ganhou! Em caso de empate, retorne Empate!"""

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    else:
        return "Player 2 won!"

# Teste

print(rps('rock', 'scissors'))
print(rps('rock', 'paper'))
print(rps('rock', 'rock'))
