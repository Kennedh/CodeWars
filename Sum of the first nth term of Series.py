"""
Sua tarefa é escrever uma função que retorna o n-ésimo termo da série a seguir,
que é a soma dos primeiros ntermos da sequência ( né o parâmetro de entrada).

Série: 1 + 1/4 + 1/7 + 1/10...

Regras
Você precisa arredondar a resposta para 2 casas decimais e retorná-la como String.

Se o valor fornecido for 0então ele deve retornar "0.00".

Você receberá apenas números naturais como argumentos.
"""

def series_sum(n):
    res = 1
    s = 4
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    else:
        for num in range(n-1):
            res += 1/s
            s += 3
        return f"{res:.2f}"

# Teste

print(series_sum(4))