"""
Hora de ganhar na loteria!

Dado um bilhete de loteria (ticket), representado por uma matriz de matrizes de 2 valores, você deve descobrir se
ganhou o prêmio máximo.

Exemplo de bilhete:

[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
Para fazer isso, você precisa primeiro contar as "minivitórias" do seu bilhete. Cada subconjunto contém uma string e um
número. Se o código de qualquer caractere da string corresponder ao número, você ganha uma minivitória. Observe que você
só pode ter uma minivitória por subconjunto.

Depois de contar todas as suas mini vitórias, compare esse número com a outra entrada fornecida (vitória). Se o seu
total for maior ou igual a (vitória), retorne "Vencedor!". Caso contrário, retorne "Perdedor!".

Todas as entradas estarão no formato correto. As strings nos tickets nem sempre têm o mesmo comprimento.
"""

def bingo(ticket,win):
    count = 0
    for a in ticket:
        for b in a[0]:
            if ord(b) == a[1]:
                count += 1
                break
    if count >= win:
        return "Winner!"
    else:
        return "Loser!"

# Teste

print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1))


