"""
Seu objetivo é criar uma função que remova o primeiro e o último caracteres de uma string. Você recebe um parâmetro,
a string original.

Importante: Sua função deve lidar com strings de qualquer comprimento ≥ 2 caracteres. Para strings com exatamente 2
caracteres, retorne uma string vazia.
"""

def remove_char(s):
    return s[1:-1]

# Teste

print(remove_char('eloquent'))