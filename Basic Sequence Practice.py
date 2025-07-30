"""
Uma sequência ou série , em matemática, é uma sequência de objetos, como números, que seguem um padrão específico. Os
elementos individuais em uma sequência são chamados de termos. Um exemplo simples é 3, 6, 9, 12, 15, 18, 21, ..., onde
o padrão é: "some 3 ao termo anterior" .

Neste kata, usaremos uma sequência mais complicada: 0, 1, 3, 6, 10, 15, 21, 28, ... Esta sequência é gerada com o
padrão: "o enésimo termo é a soma dos números de 0 a n, inclusive" .

[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3
Sua tarefa
Complete a função que recebe um inteiro ne retorna uma lista/matriz de comprimento abs(n) + 1da série aritmética
explicada acima. Quando n < 0retornar a sequência com termos negativos.
"""

def sum_of_n(n):
    res = [0]
    if n > 0:
        for x in range(1,n+1):
            res.append(x + res[-1])
    elif n < 0:
        for x in range(1,abs(n)+1):
            res.append(-abs(x) + res[-1])
    return res

# Teste

print(sum_of_n(0))
print(sum_of_n(-5))
print(sum_of_n(5))