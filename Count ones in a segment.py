"""
Dados dois números: 'esquerda' e 'direita' (1 <= 'esquerda' <= 'direita' <= 200000000000000), retorna a soma de todas as ocorrências '1' em representações binárias de números entre 'esquerda' e 'direita' (incluindo ambos)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.
AVISO: O segmento pode conter bilhões de elementos. Para passar neste kata, sua solução não pode iterar por todos os números no segmento!
"""

# Primeira versão

def count_onesv1(left, right):
    res = 0
    for n in range(left, right+1):
        res += str(bin(n)[2:]).count("1")
    return res

# Teste

print(count_onesv1(1,13))

"""Como o codewars tem limite de timeout (12000ms), e para iterar bilhões de segmentos, leva muito tempo. Eu vou precisar de
 equação para tornar o código eficiente pois atualmente ele funciona mas para grandes volumes de números ele demora.

 Equação vai consister em analisar um grande quantidade de números binarios e analisar um padrão entre eles"""

# Testando algumas possibilidades

# x é número de casas minimas binarias, usando exemplo de 0-7 são no maximo 3


# Versão final

def count_ones(left, right):
    def soma_uns_ate(n):
        if n <= 1:
            return 1 if n == 1 else 0

        x = n.bit_length() - 1
        soma_bloco_principal = x * (1 << (x - 1))
        soma_bits_restantes = n - (1 << x) + 1
        recursao = soma_uns_ate(n - (1 << x))

        return soma_bloco_principal + soma_bits_restantes + recursao

    return soma_uns_ate(right) - soma_uns_ate(left - 1)

print(count_ones(0,61401131303700))