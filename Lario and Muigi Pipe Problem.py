"""
Emitir
Parece que algum encanador bandido e seu irmão estão por aí danificando seus palcos novamente.

A pipesconexão dos estágios do seu nível precisa ser corrigida antes que você receba mais reclamações.

Eles pipesestão corretos quando cada um pipeapós o primeiro é 1maior que o anterior.

Tarefa
Dada uma lista de valores exclusivos numbersclassificados em ordem crescente,
retorne uma nova lista de modo que os valores sejam incrementados em 1 para cada índice,
do valor mínimo até o valor máximo (ambos incluídos).
"""

def pipe_fix(nums):
    return [num for num in range(nums[0],nums[-1]+1)]

# Teste

print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
print(pipe_fix([1, 2, 3, 12]))
print(pipe_fix([6, 9]))
