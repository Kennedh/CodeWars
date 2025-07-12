"""
Crie um método para verificar se a string está em LETRAS MAIÚSCULAS.
"""

def is_uppercase(inp):
    for n in inp:
        if n.isalpha():
            if n.upper() == n:
                res = True
            else:
                return False
    return True

# Teste

print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))