"""
Crie uma função que retorne o valor multiplicado por 50 e aumentado por 6.
Se o valor inserido for uma string, ela deverá retornar "Error".
"""

def problem(a):
    return (a * 50) + 6 if str(a).isdigit() else "Error"

# teste

print(problem("hello"))
print(problem(1))

