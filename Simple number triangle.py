"""
Considere o triângulo numérico abaixo, no qual cada número é igual ao número acima mais o número à esquerda. Se não
houver nenhum número acima, assuma que é um 0.

1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
O triângulo tem 5linhas e a soma da última linha é sum([1,4,9,14,14]) = 42.

Você receberá um número inteiro ne sua tarefa será retornar a soma da última linha de um triângulo de nlinhas.

No exemplo acima:

solve(5) = 42
"""

def solve(n):
    linha = [1]
    for _ in range(1, n):
        nova = [1]
        for j in range(1, len(linha)+1):
            acima = linha[j] if j < len(linha) else 0
            esquerda = nova[-1]
            nova.append(acima + esquerda)
        linha = nova
    return sum(linha)

# Teste

print(solve(20))