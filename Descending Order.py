"""
Sua tarefa é criar uma função que possa receber qualquer inteiro não negativo como argumento
e retorná-lo com seus dígitos em ordem decrescente.
Essencialmente, reorganize os dígitos para criar o maior número possível.
"""

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

# Teste

print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))