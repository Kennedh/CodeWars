"""
Você tem um jardim premiado e todos os dias as plantas precisam de exatamente 40 mm de água.
Você criou um ótimo código JavaScript para calcular a quantidade de água que suas plantas precisarão,
considerando a quantidade de chuva prevista para o dia. Seu vizinho invejoso invadiu seu computador e
inundou seu código com bugs.
test.assert_equals
Sua tarefa é depurar o código antes que suas plantas morram!
"""

def rain_amount(mm):
    if mm < 40:
         return f"You need to give your plant {40 - mm}mm of water"
    else:
         return "Your plant has had more than enough water for today!"

# Teste

print(rain_amount(100))
print(rain_amount(40))
print(rain_amount(39))
print(rain_amount(5))
print(rain_amount(0))

