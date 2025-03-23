"""
Precisamos de uma função que possa transformar uma string em um número. Quais maneiras de conseguir isso você conhece?

Nota: Não se preocupe, todas as entradas serão strings,
e cada string é uma representação perfeitamente válida de um número integral.
"""

def string_to_number(s):
    return int(s)

# Teste

print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("-7"))

