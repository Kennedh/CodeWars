"""
Bob trabalha como motorista de ônibus.
No entanto, ele se tornou extremamente popular entre os moradores da cidade.
Com tantos passageiros querendo embarcar em seu ônibus,
ele às vezes se depara com o problema de não ter espaço suficiente!
Ele quer que você escreva um programa simples informando se ele conseguirá acomodar todos os passageiros.
"""

def enough(cap, on, wait):
    res = wait - (cap - on)
    return res if res > 0 else 0