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
        temp = strng.rsplit(str(num), 1)
        res = f"{num2}".join(temp)
        if "0" in strng and strng[-1] == 9:
            res = res.replace("0","",1)
            return res
    else:
        return strng + "1"

# Teste

print(increment_string("fo99obar99"))

