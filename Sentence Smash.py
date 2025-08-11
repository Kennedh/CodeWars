"""
Frase Quebrada
Escreva uma função que receba um array de palavras e as junte em uma frase, retornando-a. Você pode ignorar a
necessidade de sanitizar palavras ou adicionar pontuação, mas deve adicionar espaços entre cada palavra. Cuidado, não deve haver espaço no início ou no final da frase!

Exemplo
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
Suposições
Você pode assumir que só lhe são dadas palavras.
Você não pode presumir o tamanho do array.
Você pode assumir que obtém uma matriz.
O que estamos testando
Estamos testando loops básicos e manipulação de strings. Este tutorial é para iniciantes que estão aprendendo loops e
manipulação de strings.
"""

def smash(words):
    return ' '.join(words)

# Teste

print(smash(["hello", "amazing", "world"]))