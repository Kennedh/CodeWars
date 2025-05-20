"""
Seu trabalho é escrever uma função que incrementa uma string para criar uma nova string.

Se a sequência já terminar com um número, o número deverá ser incrementado em 1.
Se a sequência não terminar com um número, o número 1 deverá ser acrescentado à nova sequência.
"""
from dataclasses import replace


def increment_string(strng):
    rev = strng[::-1]
    num = ""
    if rev[0].isdigit():
        for idx, l in enumerate(rev):
            if (l.isdigit() and idx == 0) or (l.isdigit() and l != "0"):
                num += l
            else:
                break
        num2 = int(num[::-1]) + 1
        res = strng
        res = res.replace(num[::-1], str(num2))
        return res
    else:
        return strng + "1"

# Teste

print(increment_string("foobar001"))

