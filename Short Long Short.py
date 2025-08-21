"""
Dadas duas strings, ae b, retorna uma string no formato short+long+short, com a string mais curta na parte externa e a
mais longa na parte interna. As strings não terão o mesmo comprimento, mas podem estar vazias ( zerolength ).

Dica para usuários de R:

O comprimento da string nem sempre é o mesmo que o número de caracteres
"""

def solution(a, b):
    return b + a + b if len(a) > len(b) else a + b + a

# Teste

print(solution("aaaa","a"))
print(solution("a", "aaaaa"))

print(solution("",""))