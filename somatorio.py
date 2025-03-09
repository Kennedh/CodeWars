"""Escreva um programa que encontre a soma de cada número de 1 a num.
O número sempre será um inteiro positivo maior que 0. Sua função só precisa retornar o resultado,
o que é mostrado entre parênteses no exemplo abaixo é como você chega a esse resultado e não faz parte dele,
veja os testes de exemplo."""

def summation(num):
    return sum(range(1, num + 1))

# Teste

print(summation(5))
print(summation(10))