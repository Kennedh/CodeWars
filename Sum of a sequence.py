"""
Sua tarefa é escrever uma função que retorna a soma de uma sequência de números inteiros.

A sequência é definida por 3 valores não negativos: begin , end , step .

Se o valor begin for maior que o end , sua função deverá retornar 0. Se end não for o resultado de um número inteiro de
passos, não o adicione à soma. Veja o quarto exemplo abaixo.
"""

def sequence_sum(begin_number, end_number, step):
    return sum([n for n in range(begin_number, end_number+1, step)])

# Teste

print(sequence_sum(2,8,1))
print(sequence_sum(0, 15, 3))

