"""
Um formato para expressar uma lista ordenada de inteiros é usar uma lista separada por vírgulas de

inteiros individuais
ou um intervalo de inteiros denotado pelo inteiro inicial separado do inteiro final do intervalo por um hífen, '-'.
O intervalo inclui todos os inteiros no intervalo, incluindo ambos os pontos finais.
Não é considerado um intervalo a menos que abranja pelo menos 3 números. Por exemplo, "12,13,15-17"
Complete a solução para que ela receba uma lista de números inteiros em ordem crescente e
retorne uma string formatada corretamente no formato de intervalo.

"""

def solution(args):
    res = []
    i = 0
    while i < len(args):
        inicio = i
        while i + 1 < len(args) and args[i + 1] == args[i] + 1:
            i += 1
        if i - inicio >= 2:
            res.append(f"{args[inicio]}-{args[i]}")
        else:
            for j in range(inicio, i + 1):
                res.append(str(args[j]))
        i += 1
    return ",".join(res)

li = [1,2]

# Teste

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))