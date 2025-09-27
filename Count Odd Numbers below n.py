"""
Dado um número n, retorne o número de números ímpares positivos abaixo n, FÁCIL!

Exemplos (Entrada -> Saída)
7  -> 3 (because odd numbers below 7 are [1, 3, 5])
15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])
Espere grandes entradas!
"""

def odd_count(n):
    return n // 2

# Teste

print(odd_count(15))
print(odd_count(15023))
