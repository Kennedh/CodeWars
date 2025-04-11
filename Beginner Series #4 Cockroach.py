"""
A barata é um dos insetos mais rápidos.
Escreva uma função que receba sua velocidade em km por hora e a retorne em cm por segundo,
arredondada para o número inteiro (= pisou).
"""

def cockroach_speed(s):
    return int((((s*1000)*100)/60)/60) # km > m > cm / hr > min > seg

# Acredito que tenha alguma forma mais facil de fazer mas essa for a primeira logica que veio na minha cabeça

# Teste

print(cockroach_speed(1.08))
print(cockroach_speed(2.5))

