"""
Nathan adora andar de bicicleta.

Como Nathan sabe que é importante se manter hidratado, ele bebe 0,5 litro de água por hora de ciclismo.

Você recebe o tempo em horas e precisa retornar o número de litros que Nathan beberá, arredondado para baixo .
"""

def litres(time):
    return int(time*0.5)

# Teste

print(litres(5))