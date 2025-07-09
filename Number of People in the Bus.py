"""
Há um ônibus circulando pela cidade que pega e deixa algumas pessoas em cada ponto.

Você recebe uma lista (ou array) de pares de inteiros. Os elementos de cada par representam o número de pessoas que
entram no ônibus (o primeiro item) e o número de pessoas que descem (o segundo item) em um ponto de ônibus.

Sua tarefa é retornar o número de pessoas que ainda estão no ônibus após o último ponto (após a última matriz). Mesmo
que seja o último ponto, o ônibus pode não estar vazio e algumas pessoas ainda podem estar dentro do ônibus,
provavelmente dormindo lá :D

Dê uma olhada nos casos de teste.

Tenha em mente que os casos de teste garantem que o número de pessoas no ônibus seja sempre >= 0. Portanto, o inteiro
retornado não pode ser negativo.

O segundo valor no primeiro par da matriz é 0, pois o ônibus está vazio no primeiro ponto de ônibus.
"""

def number(bus_stops):
    current = 0
    for es in bus_stops:
        current += es[0]
        current -= es[1]
    return current

# Teste

print(number([[10,0],[3,5],[5,8]]))