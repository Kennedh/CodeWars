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

def count_ones(left, right):
    res = 0
    for n in range(left, right+1):
        res += str(bin(n)[2:]).count("1")
    return res

# Teste

print(count_ones(1,10000))

