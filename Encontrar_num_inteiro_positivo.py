"""
Alguns números têm propriedades engraçadas. Por exemplo:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Dados dois números inteiros positivos n e p, queremos encontrar um número inteiro positivo k, se existir,
tal que a soma dos dígitos de n elevado a potências consecutivas começando em p seja igual a k * n.

Em outras palavras, escrevendo os dígitos consecutivos de ncomo a, b, c, d ..., existe um inteiro k.

Se for o caso retornaremos k, se não retornaremos -1.

Nota : ne psempre serão inteiros estritamente positivos.
"""
#Esse codigo foi realmente dificil de fazer e entender mas vamos lá. Tentei explicar ele também conforme entendi

def dig_pow(n, p):
    # A variavel digits irá converter o n para uma lista de digitos
    digits = [int(d) for d in str(n)]

    # Aqui o total irá calcular a soma dos dígitos elevados às potências consecutivas deles
    total = sum(d ** (p + i) for i, d in enumerate(digits))

    # Essa condição serve verificar se o total é um múltiplo de n
    if total % n == 0:
        #Aqui retornará n ou -1 se não tiver nenhum número positivo inteiro
        return total // n  # Retorna k
    else:
        return -1

# Alguns testes para validar a função
print(dig_pow(89, 1))   # Saída: 1
print(dig_pow(695, 2))  # Saída: 2
print(dig_pow(46288, 3)) # Saída: 51
print(dig_pow(92, 1))   # Saída: -1


