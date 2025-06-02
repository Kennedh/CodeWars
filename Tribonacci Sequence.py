"""
Bem-vindo ao irmão mais velho de Fibonacci, também conhecido como Tribonacci.

Como o nome já pode revelar, funciona basicamente como um Fibonacci,
mas somando os últimos 3 (em vez de 2) números da sequência para gerar o próximo.
E, pior ainda, infelizmente não poderei ouvir falantes não nativos de italiano tentando pronunciá-lo :(

Então, se quisermos iniciar nossa sequência de Tribonacci com
[1, 1, 1] uma entrada inicial (também conhecida como assinatura ), temos esta sequência:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
Mas e se começássemos com [0, 0, 1]como assinatura? Como começar com, [0, 1]em vez de
[1, 1]basicamente deslocar a sequência de Fibonacci comum em uma posição,
você pode ficar tentado a pensar que obteríamos a mesma sequência deslocada em duas posições, mas esse não é o caso,
e obteríamos:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Bem, você já deve ter adivinhado, mas para deixar claro: você precisa criar uma função de Fibonacci que,
dada uma matriz/lista de assinaturas , retorne os primeiros n elementos — assinatura incluída — da sequência semeada.

A assinatura sempre conterá 3 números; n sempre será um número não negativo; se n == 0, então retorne um array vazio
(exceto em C que retorna NULL) e esteja pronto para qualquer outra coisa que não esteja claramente especificada ;)
"""

def tribonacci(signature, n):
    n0 = signature[0]
    n1 = signature[1]
    n2 = signature[2]
    res = signature
    if n == 0:
        return []
    else:
        for num in range(n):
            nxt = n0 + n1 + n2
            res.append(nxt)
            n0, n1, n2 = n1, n2, nxt
        return res[:n]

# teste

print(tribonacci([1, 1, 1], 10))