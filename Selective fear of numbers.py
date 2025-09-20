"""
Eu tenho uma doença mental muito louca. Não gosto muito de números. Mas é um pouco complicado: o número do qual tenho
medo depende do dia da semana... Esta é uma descrição concreta da minha doença mental:

Segunda-feira --> 12

Terça-feira --> números maiores que 95

Quarta-feira --> 34

Quinta-feira --> 0

Sexta-feira --> números divisíveis por 2

Sábado --> 56

Domingo --> 666 ou -666

Escreva uma função que receba uma string (dia da semana) e um inteiro (número a ser testado) para informar ao médico
se estou com medo ou não. (retorne um booleano)
"""

def am_i_afraid(day, num):
    if day == "Monday" and num == 12:
        return True
    elif day == "Tuesday" and num > 95:
        return True
    elif day == "Wednesday" and num == 34:
        return True
    elif day == "Thursday" and num == 0:
        return True
    elif day == "Friday" and num % 2 == 0:
        return True
    elif day == "Saturday" and num == 56:
        return True
    elif day == "Sunday" and (num == 666 or num == -666):
        return True
    else:
        return False

# Teste

print(am_i_afraid('Monday',   13))
print(am_i_afraid('Sunday', -666))

