"""
Sua equipe está escrevendo um novo editor de texto sofisticado e você foi encarregado de implementar a numeração de linhas.

Escreva uma função que pegue uma lista de strings e retorne cada linha precedida pelo número correto.

A numeração começa em 1. O formato é n: string. Observe os dois pontos e o espaço entre eles.
"""

def number(lines):
    res = []
    for idx, item in enumerate(lines,start=1):
        res.append(f"{idx}: {item}")
    return res

# Teste

print(number(["a", "b", "c"]))