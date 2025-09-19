"""
O zodíaco chinês é um ciclo repetitivo de 12 anos, com cada ano sendo representado por um animal e seus atributos. O
calendário lunar é dividido em ciclos de 60 anos cada, e cada ano tem uma combinação de um animal e um elemento. Há 12
animais e 5 elementos; os animais mudam a cada ano, e os elementos mudam a cada 2 anos. O ciclo atual foi iniciado no
ano de 1984, que foi o ano do Rato de Madeira.

Como o calendário atual é gregoriano, usarei apenas anos a partir da época de 1924. Para simplificar, estou contando o
ano como um ano inteiro e não de janeiro/fevereiro até o final do ano.

Tarefa
Dado um ano, retorne o elemento e o animal que esse ano representa ("Animal do Elemento"). Por exemplo, nasci em 1998,
então sou um "Tigre de Terra".

animals(ou $animalsem Ruby) é um array pré-carregado contendo os animais em ordem:

["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

elements(ou $elementsem Ruby) é um array pré-carregado contendo os elementos em ordem:

["Wood", "Fire", "Earth", "Metal", "Water"]

Conte-me seu signo e elemento do zodíaco nos comentários. Boa programação :)
"""

def chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]

    offset = year - 1984
    animal = animals[offset % 12]
    element = elements[(offset % 10) // 2]

    return f"{element} {animal}"

# Teste

print(chinese_zodiac(1998))
print(chinese_zodiac(2025))