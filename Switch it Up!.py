"""
Quando receber um número entre 0 e 9, retorne-o por extenso.
Observe que a entrada estará garantidamente dentro do intervalo de 0 a 9.
"""

def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"

# Teste

print(switch_it_up(2))