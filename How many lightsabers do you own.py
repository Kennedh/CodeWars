"""
Inspirado pela equipe de desenvolvimento da Vooza, escreva a função que

aceita o nome de um programador e
retorna o número de sabres de luz que aquela pessoa possui.
Aliás, a única pessoa que possui sabres de luz é o Zach. Ele tem 18, o que é um número impressionante de sabres de luz.
Qualquer outra pessoa possui 0.

Nota : sua função deve ter um parâmetro padrão.
"""

def how_many_light_sabers_do_you_own(name=""):
    return 0 if name != "Zach" else 18

# Teste

print(how_many_light_sabers_do_you_own("Zach"))
print(how_many_light_sabers_do_you_own("zach"))
print(how_many_light_sabers_do_you_own())