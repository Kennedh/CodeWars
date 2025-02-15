# Nesta tarefa, você recebe um número e tem que torná-lo negativo. Se for negativo ou zero não faz nada

def make_negative(number):
    if number > 0:
        number *= -1

    return number

# teste

number = -5
print(make_negative(number))