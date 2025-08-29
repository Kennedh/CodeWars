"""
Um primo de Mersenne é um número primo que pode ser representado como: M n = 2 n - 1. Portanto, todo primo de
Mersenne é um a menos que uma potência de dois.

Escreva uma função que retornará se o inteiro fornecido nproduzirá um primo de Mersenne ou não.

Os testes verificarão números inteiros aleatórios até 2000.


"""


def is_prime(n):
    if n < 2:
        return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def valid_mersenne(n):
    if n <= 1 or not is_prime(n):
        return False
    return is_prime(2 ** n - 1)

# Teste

print(valid_mersenne(127))