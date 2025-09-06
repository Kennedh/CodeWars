"""
Quem se lembra do tempo em que estávamos no pátio da escola, quando as meninas pegavam uma flor e arrancavam suas
pétalas, dizendo cada uma das seguintes frases cada vez que uma pétala era arrancada:

"Eu te amo"
"um pouco"
"bastante"
"apaixonadamente"
"loucamente"
"de jeito nenhum"
Se houver mais de 6 pétalas, você recomeça com "I love you"7 pétalas, "a little"com 8 pétalas e assim por diante.

Quando a última pétala foi arrancada, houve gritos de excitação, sonhos, pensamentos e emoções crescentes.

Seu objetivo neste kata é determinar qual frase as meninas diriam na última pétala de uma flor com um determinado
número de pétalas. O número de pétalas é sempre maior que 0.
"""

def how_much_i_love_you(nb_petals):
    op = ["I love you",
          "a little",
          "a lot",
          "passionately",
          "madly",
          "not at all"]
    index = (nb_petals - 1) % len(op)
    return op[index]

# Teste

print(how_much_i_love_you(30))