"""
Desta vez, queremos escrever cálculos usando funções e obter os resultados. Vejamos alguns exemplos:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requisitos:

Deve haver uma função para cada número de 0 ("zero") a 9 ("nove")
Deve haver uma função para cada uma das seguintes operações matemáticas: mais, menos, vezes, dividido_por
Cada cálculo consiste em exatamente uma operação e dois números
A função mais externa representa o operando esquerdo, a função mais interna representa o operando direito
A divisão deve ser uma divisão inteira . Por exemplo, isso deve retornar 2, não 2.666666...:
eight(divided_by(three()))
"""

def zero(op=None):
    if op:
        return op(0)
    return 0
def one(op=None):
    if op:
        return op(1)
    return 1
def two(op=None):
    if op:
        return op(2)
    return 2
def three(op=None):
    if op:
        return op(3)
    return 3
def four(op=None):
    if op:
        return op(4)
    return 4
def five(op=None):
    if op:
        return op(5)
    return 5
def six(op=None):
    if op:
        return op(6)
    return 6
def seven(op=None):
    if op:
        return op(7)
    return 7
def eight(op=None):
    if op:
        return op(8)
    return 8
def nine(op=None):
    if op:
        return op(9)
    return 9

def plus(right):
    return lambda left: left + right
def minus(right):
    return lambda left: left - right
def times(right):
    return lambda left: left * right
def divided_by(right):
    return lambda left: left // right

# Teste

print(eight(divided_by(eight())))