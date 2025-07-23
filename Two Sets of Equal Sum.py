"""Se possível, divida os inteiros 1,2,…,n em dois conjuntos de soma igual.

Entrada
Um inteiro positivo n <= 1.000.000.

Saída
Se não for possível, retorne [ ] (Python, Javascript, Swift, Ruby) ou ( ) (Python) ou [ [],[] ] (Java, C#, C++, Kotlin)
ou None (Scala) ou Nothing (Haskell) ou nil (Lua).
Se for possível, retorne dois conjuntos disjuntos. Cada inteiro de 1 a n deve estar em um deles. Os inteiros do primeiro
conjunto devem somar o mesmo valor que os inteiros do segundo conjunto. Os conjuntos podem ser retornados em uma tupla,
lista ou array, dependendo da linguagem.

Exemplos:
Para n = 8, as respostas válidas incluem:
[1, 3, 6, 8], [2, 4, 5, 7] (ou [[1, 3, 6, 8], [2, 4, 5, 7]])
[8, 1, 3, 2, 4], [5, 7, 6]
[7, 8, 3], [6, 1, 5, 4, 2] e outras.

Para n = 9, isso não é possível. Por exemplo, tente [6, 8, 9] e [1, 2, 3, 4, 5, 7], mas o primeiro soma 23 e o segundo,
22. Nenhum outro conjunto funciona."""

def create_two_sets_of_equal_sum(n):
    soma = n * (n + 1) // 2
    if soma % 2 != 0:
        return []

    target = soma // 2
    a, b = [], []

    for num in range(n, 0, -1):
        if num <= target:
            a.append(num)
            target -= num
        else:
            b.append(num)
    return [a, b]

# Teste

print(create_two_sets_of_equal_sum(8))