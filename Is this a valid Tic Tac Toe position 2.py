"""
Você trabalha como cientista de dados em uma empresa de TI e, de repente, seu chefe pediu para você encontrar os padrões
mais comuns em jogos da velha enviados para uma pesquisa no site da sua empresa.

Entretanto, algumas delas não são de jogos reais, ou seja, a posição em tal tabuleiro não pode ser alcançada por meio
de jogo normal.

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
Se todos os quadrados estiverem ocupados e nenhum jogador conseguir formar uma fileira de 3 peças, o jogo termina
empatado (o que é válido).
Jogos em que nem todos os quadrados estão ocupados e nenhum jogador conseguiu 3 em sequência são considerados válidos.
Caso especial : Este tabuleiro (e outros similares onde 'X' tem duas três em linha, mas a posição pode ser alcançada):

X X X
O O X
O O X
deve resultar em true.

O tabuleiro tem a garantia de ter dimensões 3x3 e consistir apenas de 'X', 'O' ou '_'.
"""

def is_valid_position(board):
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if not (x_count == o_count or x_count == o_count + 1):
        return False

    def count_wins(board):
        x_wins = 0
        o_wins = 0

        for row in board:
            if all(cell == 'X' for cell in row):
                x_wins += 1
            if all(cell == 'O' for cell in row):
                o_wins += 1

        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                x_wins += 1
            if all(board[row][col] == 'O' for row in range(3)):
                o_wins += 1

        if all(board[i][i] == 'X' for i in range(3)):
            x_wins += 1
        if all(board[i][i] == 'O' for i in range(3)):
            o_wins += 1

        if all(board[i][2 - i] == 'X' for i in range(3)):
            x_wins += 1
        if all(board[i][2 - i] == 'O' for i in range(3)):
            o_wins += 1

        return x_wins, o_wins

    x_wins, o_wins = count_wins(board)

    if x_wins > 0 and o_wins > 0:
        return False

    if o_wins > 0 and x_count != o_count:
        return False

    if x_wins > 0 and x_count != o_count + 1:
        return False

    if x_wins > 1 and x_count != o_count + 1:
        return False

    return True


# Teste

print(is_valid_position((
                ('O', 'O', 'O'),
                ('X', 'X', 'X'),
                ('_', '_', 'X'),
            )))

