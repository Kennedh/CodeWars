"""
Queremos criar uma função que some números quando chamada em sucessão.

add(1)(2) # equals 3
Também queremos poder continuar a adicionar números à nossa cadeia.

add(1)(2)(3) # 6
add(1)(2)(3)(4); # 10
add(1)(2)(3)(4)(5) # 15
e assim por diante.

Uma única chamada deve ser igual ao número passado.

add(1) # 1
Deveríamos ser capazes de armazenar os valores retornados e reutilizá-los.

addTwo = add(2)
addTwo # 2
addTwo + 5 # 7
addTwo(3) # 5
addTwo(3)(5) # 10
Podemos assumir que qualquer número passado será um número inteiro válido.
"""

class Adder:
    def __init__(self, total):
        self.total = total

    def __call__(self, x=None):
        if x is None:
            return self.total
        if isinstance(x, Adder):
            return Adder(self.total + x.total)
        return Adder(self.total + x)

    def __int__(self):
        return self.total

    def __str__(self):
        return str(self.total)

    def __repr__(self):
        return str(self.total)

    def __add__(self, other):
        return self.total + other

    def __eq__(self, other):
        if isinstance(other, Adder):
            return self.total == other.total
        return self.total == other

def add(n):
    return Adder(n)


a = add(1)
b = a(2)
c = b(3)

print(c == 6)

