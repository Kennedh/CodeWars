"""
Dados três inteiros a, b, e c, retorna o maior número obtido após a inserção dos operadores +, *e parênteses (). Em
outras palavras, tente todas as combinações de a, b, e ccom os operadores, sem reordenar os operandos, e retorne o valor
máximo.

Exemplo
Com os números 1, 2 e 3, aqui estão algumas expressões possíveis:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
O valor máximo que pode ser obtido é 9.

Notas
Os números são sempre positivos, no intervalo 1 ≤ a, b, c ≤ 10.
Você pode usar a mesma operação mais de uma vez.
Não é necessário usar todos os operadores ou parênteses.
Não é possível trocar os operandos. Por exemplo, com os números fornecidos, não é possível obter
a expressão (1 + 3) * 2 = 8.

Exemplos de entrada e saída

expressionsMatter(1, 2, 3) ==> 9, porque (1 + 2) * 3 = 9.
expressionsMatter(1, 1, 1) ==> 3, porque 1 + 1 + 1 = 3.
expressionsMatter(9, 1, 1) ==> 18, porque 9 * (1 + 1) = 18.
"""

def expression_matter(a, b, c):
    eq1 = a * (b + c)
    eq2 = a * b * c
    eq3 = a + b * c
    eq4 = (a + b) * c
    eq5 = a + b + c
    return max(eq1, eq2, eq3, eq4, eq5)

# Teste

print(expression_matter(1, 1, 1))
