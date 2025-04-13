"""
Escreva uma função que receba um array de números (inteiros para os testes) e um número alvo.
Ela deve encontrar dois itens diferentes no array que, quando somados, resultem no valor alvo.
Os índices desses itens devem ser retornados em uma tupla/lista (dependendo da sua linguagem) como: (índice1, índice2).

Para os fins deste kata, alguns testes podem ter múltiplas respostas; quaisquer soluções válidas serão aceitas.

A entrada será sempre válida (os números serão um array de comprimento 2 ou maior, e todos os itens serão números;
o alvo será sempre a soma de dois itens diferentes desse array).
"""

def two_sum(numbers, target):
    for idx_one, n in enumerate(numbers):
        for idx_two, num in enumerate(numbers):
            if n + num == target and idx_one != idx_two:
                return idx_one, idx_two



# Teste

print(two_sum([1 ,2, 3],4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2, 2, 3],4))

