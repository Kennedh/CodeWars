"""
Tarefa:
Você precisa escrever uma função patternque retorne o seguinte Padrão (veja Padrão e Exemplos) até no número de linhas.

Observação: Returningo padrão não é o mesmo que Printingo padrão.
Regras/Nota:
Se n < 1então ele deve retornar "", ou seja, uma string vazia.
Estão no whitespacesno padrão.
Padrão:
(n)(n-1)(n-2)...4321
(n)(n-1)(n-2)...432
(n)(n-1)(n-2)...43
(n)(n-1)(n-2)...4
...............
..............
(n)(n-1)(n-2)
(n)(n-1)
(n)
Exemplos:
padrão(4):

4321
432
43
4
padrão(11):

1110987654321
111098765432
11109876543
1110987654
111098765
11109876
1110987
111098
11109
1110
11
Dica: Use \n na string para pular para a próxima linha

"""

def pattern(n):
    res = ""
    c = 0
    if n <= 0:
        return ""
    for a in range(n+1):
        for i in range(n,0 + c,-1):
            res += str(i)
        c += 1
        if c == n:
            break
        else:
            res += "\n"
    return res

# Teste

print(pattern(1))
print(pattern(25))
print(pattern(-8))
print(pattern(0))

