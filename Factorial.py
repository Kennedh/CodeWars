"""
Sua tarefa é escrever a função factorial.
"""

def factorial(n):
    res = 1
    for n in range(n,0,-1):
        if res == 1:
            res = n
        else:
            res *= n
    return res

# Teste

print(factorial(5))