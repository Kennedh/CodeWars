"""
O número 89 é o primeiro inteiro com mais de um dígito que preenche a propriedade parcialmente introduzida
no título deste kata. Qual a utilidade de dizer "Eureka"? Porque esta soma resulta no mesmo número: 89 = 8¹ + 9²

O próximo número a possuir esta propriedade é 135:

Veja esta propriedade novamente: 135 = 1¹ + 3² + 5³

Tarefa
Precisamos de uma função para coletar esses números, que pode receber dois inteiros a, b que definem o intervalo [a, b]
(inclusive) e gera uma lista dos números ordenados no intervalo que preenche a propriedade descrita acima.
"""

def sum_dig_pow(a, b):
    temp = 0
    res = []
    for n in range(a, b + 1):
        temp = 0
        for x, y in enumerate(str(n)):
            temp += int(y) ** (x + 1)
        if temp == n:
            res.append(n)
    return res

# Teste

print(sum_dig_pow(89, 135))
print(sum_dig_pow(90, 100))
print(sum_dig_pow(1, 100))


