"""
O sapo-de-boca-larga está particularmente interessado nos hábitos alimentares de outras criaturas.

Ele simplesmente não consegue parar de perguntar às criaturas que encontra o que elas gostam de comer. Mas então ele
conhece o jacaré que ADORA comer sapos de boca larga!

Quando ele encontra o jacaré, ele então faz uma pequena boca.

Seu objetivo neste kata é criar um mouth_size metodo completo. Este metodo recebe um argumento animal que corresponde ao
animal encontrado pelo sapo. Se este for um alligator(sem distinção de maiúsculas e minúsculas), return , smallcaso
contrário, return wide.
"""

def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"

# Teste

print(mouth_size("toucan"))
print(mouth_size("alligator"))