"""
Implemente uma função que aceite 3 valores inteiros a, b, c.
A função deve retornar true se um triângulo puder ser construído com os lados de comprimento dado
e false em qualquer outro caso.

(Neste caso, todos os triângulos devem ter superfície maior que 0 para serem aceitos).
"""

def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

# Para ser um triangulo além de todos os lados serem maior que zero, a soma de dois lados tem que ser maior que o 3º

# Teste

print(is_triangle(1,2,3))
print(is_triangle(1,2,2))
print(is_triangle(4,2,3))
print(is_triangle(2,2,2))
print(is_triangle(-5,1,3))

