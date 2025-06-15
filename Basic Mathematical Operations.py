"""
Sua tarefa é criar uma função que execute quatro operações matemáticas básicas.

A função deve receber três argumentos: operação(string/caractere), valor1(número), valor2(número).
A função deve retornar o resultado em números após aplicar a operação escolhida.
"""

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "/":
        return value1 / value2
    else:
        return value1 * value2

# Teste

print(basic_op('/', 49, 7))
print(basic_op('*', 5, 5))
print(basic_op('-', 15, 18))
print(basic_op('+', 4, 7))