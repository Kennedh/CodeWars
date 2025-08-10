"""
Você trabalha como cientista de dados em uma empresa de TI e, de repente, seu chefe pediu para você encontrar os padrões
mais comuns em jogos da velha enviados para uma pesquisa no site da sua empresa.

Entretanto, algumas delas não são de jogos reais, ou seja, a posição em tal tabuleiro não pode ser alcançada por meio de
jogo normal.

Você precisa encontrar uma maneira de filtrar esses "jogos", deixando apenas os corretos (alcançáveis).

Tarefa
Você receberá uma lista 3x3 de caracteres (veja a Solução Inicial e os Testes de Exemplo para a codificação específica
usada em seu idioma) representando um tabuleiro de jogo da velha, com as seguintes especificações:

'X' é um quadrado ocupado pelo jogador X,
'O' é uma casa ocupada pelo jogador O,
'_' é um quadrado não ocupado por nenhum jogador.
Dado este tabuleiro, você precisa determinar se ele representa uma posição que pode ser alcançada através do jogo normal
e retornar um valor booleano: true(se a condição for satisfeita) e falsecaso contrário.

Regras de validação :

'X' deve ser sempre o primeiro jogador a se mover.
Durante um movimento, um jogador deve ocupar um quadrado extra.
Se um jogador conseguir ocupar 3 quadrados em uma fileira (horizontal, vertical ou diagonal), o jogo termina
imediatamente e nenhum outro movimento pode ser feito; esse jogador vence e é declarado vitorioso (tal jogo é válido).
Se todos os quadrados estiverem ocupados e nenhum jogador conseguir formar 3 em sequência, o jogo termina empatado (o
que é válido).
Jogos em que nem todos os quadrados estão ocupados e nenhum jogador conseguiu 3 em sequência são considerados válidos.
Caso especial : Este tabuleiro (e outros similares onde 'X' tem duas três em linha, mas a posição pode ser alcançada):

X X X
O O X
O O X
deve resultar em true.
"""

def venceu(jogador, board):
    for linha in board:
        if all(casa == jogador for casa in linha):
            return True
    if all(board[i][i] == jogador for i in range(2,0,-1)):
        return True
    if all(board[i][i] == jogador for i in range(len(board))):
        return True
    return False

# Teste

print(venceu("X",[
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]))

