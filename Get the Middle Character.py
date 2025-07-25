"""
Você receberá uma string não vazia . Sua tarefa é retornar o(s) caractere(s) do meio da string.

Se o comprimento da string for ímpar, retorne o caractere do meio.
Se o comprimento da string for par, retorne os 2 caracteres do meio.
"""

def get_middle(s):
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return s[mid - 1:mid + 1]
    if n % 2 != 0:
        return s[mid:mid + 1]

# Teste

print(get_middle("abcde"))