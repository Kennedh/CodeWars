"""
O Western Suburbs Croquet Club tem duas categorias de membros, Sênior e Aberto.
Eles gostariam da sua ajuda com um formulário de inscrição
que informará aos possíveis membros em qual categoria eles serão colocados.

Para ser sênior, um membro deve ter pelo menos 55 anos e ter um handicap maior que 7.
Neste clube de croquet, os handicaps variam de -2 a +26; quanto melhor o jogador, menor o handicap.

Entrada
A entrada consistirá em uma lista de pares. Cada par contém informações para um único membro potencial.
As informações consistem em um inteiro para a idade da pessoa e um inteiro para o handicap da pessoa.
"""

def open_or_senior(data):
    res = []
    for os in data:
        if os[0] >= 55 and os[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res

# Teste

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))