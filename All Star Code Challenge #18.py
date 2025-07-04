"""
Crie uma função que aceite uma string e um único caractere e retorne um inteiro igual à contagem de ocorrências em que o
segundo argumento for encontrado no primeiro.

Se nenhuma ocorrência for encontrada, uma contagem de 0deverá ser retornada.
"""

def str_count(strng, letter):
    return strng.count(letter)

# Teste

print(str_count('hello', 'l'))