"""
Instruções
Escreva uma função que receba uma única string não vazia contendo apenas letras ASCII maiúsculas e minúsculas ( word)
como argumento e retorne uma lista ordenada contendo os índices de todas as letras maiúsculas na string.

Exemplo (Entrada --> Saída)
"CodEWaRs" --> [0,3,4,6]
"""

def capitals(word):
    res = []
    for idx, letter in enumerate(word):
        if letter == letter.upper():
            res.append(idx)
    return res

# Teste

print(capitals('CodEWaRs'))