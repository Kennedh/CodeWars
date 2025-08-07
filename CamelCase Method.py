"""
Escreva um método (ou função, dependendo da linguagem) que converta uma string para camelCase, ou seja, todas as
palavras devem ter a primeira letra maiúscula e os espaços devem ser removidos.

Exemplos (entrada --> saída):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
"""

def camel_case(s):
    res = [w.title() for w in s.split()]
    return "".join(res)

# Teste

print(camel_case("camel case method"))