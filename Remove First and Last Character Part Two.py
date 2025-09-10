"""
Este é um desdobramento do meu primeiro kata .

Você recebe uma string contendo uma sequência de caracteres separados por vírgulas.

Escreva uma função que retorna uma nova string contendo as mesmas sequências de caracteres, exceto a primeira e a
última, mas desta vez separadas por espaços.

Se a string de entrada estiver vazia ou a remoção do primeiro e do último itens fizer com que a string resultante fique
vazia, retorne um valor vazio (representado como um valor genérico NULLnos exemplos abaixo).
"""

def array(string):
    if not string:
        return None
    partes = string.split(',')

    if len(partes) <= 2:
        return None

    meio = partes[1:-1]

    return ' '.join(meio)

# Teste

print(array("1,2,3"))