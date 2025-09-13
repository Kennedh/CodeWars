"""
Meu avô sempre previu a idade das pessoas e, pouco antes de falecer, revelou seu segredo!

Em homenagem à memória do meu avô, escreveremos uma função usando sua fórmula!

Faça uma lista das idades em que cada um dos seus bisavós morreu.
Multiplique cada número por ele mesmo.
Some tudo.
Calcule a raiz quadrada do resultado.
Divida por dois.
Exemplo
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Observação: o resultado deve ser arredondado para o número inteiro mais próximo.

Alguns testes aleatórios podem falhar devido a um bug na implementação do JavaScript. Basta reenviar se isso acontecer
com você.
"""

def predict_age(*ages):
    res = 0
    for age in ages:
        res += age * age
    res = res ** 0.5
    res = res // 2
    return res

# Teste

print(predict_age(79,54,59,89,52,53,85,61))