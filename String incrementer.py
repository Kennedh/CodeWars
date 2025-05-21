"""
Seu trabalho é escrever uma função que incrementa uma string para criar uma nova string.

Se a sequência já terminar com um número, o número deverá ser incrementado em 1.
Se a sequência não terminar com um número, o número 1 deverá ser acrescentado à nova sequência.
"""
from dataclasses import replace


def increment_string(strng):
    if strng and strng[-1].isdigit():
        i = len(strng) - 1
        while i >= 0 and strng[i].isdigit():
            i -= 1
        prefix = strng[:i + 1]
        num_part = strng[i + 1:]
        incremented = str(int(num_part) + 1).zfill(len(num_part))
        return prefix + incremented
    elif not strng:
        return "1"
    else:
        return strng + "1"

# Teste

print(increment_string("sadsadas099"))

