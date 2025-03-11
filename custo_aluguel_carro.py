"""Depois de um trimestre difícil no escritório, você decide descansar um pouco nas férias.
Então, você vai reservar um voo para você e sua namorada e tentar deixar toda a bagunça para trás.

Você precisará alugar um carro para se locomover nas suas férias.
O gerente da locadora de veículos faz algumas boas ofertas para você.

Cada dia que você aluga o carro custa $ 40.
Se você alugar o carro por 7 ou mais dias, você ganha $ 50 de desconto no total.
Alternativamente, se você alugar o carro por 3 ou mais dias, você ganha $ 20 de desconto no total.

Escreva um código que forneça o valor total para diferentes dias(d)."""

def rental_car_cost(d):
    if d >= 7:
        cost = (d * 40) - 50
    elif d >= 3:
        cost = (d * 40) - 20
    else:
        cost = d * 40

    return cost