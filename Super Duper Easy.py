"""
Crie uma função que retorne o valor multiplicado por 50 e aumentado por 6.
Se o valor inserido for uma string, ela deverá retornar "Error".
"""

def problem(a):
    return "Error" if isinstance(a,str) else a * 50 + 6

# teste

print(problem("hello"))
print(problem(1))

