"""
Crie uma função que receba 2 números inteiros em forma de string como entrada e gere a soma (também como string):
"""

def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    return str(int(a) + int(b))

# Teste

print(sum_str("88","45"))
