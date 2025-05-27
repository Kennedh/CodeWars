"""
Jamie é programadora e namorada de James.
Ela gosta de diamantes e quer um colar de diamantes de James. Como James não sabe como fazer isso,
ele precisa da sua ajuda.

Tarefa
Você precisa retornar uma string que se assemelhe a um diamante quando impressa na tela, usando caracteres asterisco(\*.
Espaços à direita devem ser removidos e cada linha deve ser terminada com um caractere de nova linha ( \n).

Retorna null/nil/None/...se a entrada for um número par ou negativo,
pois não é possível imprimir um losango de tamanho par ou negativo.
"""

def diamond(n):
    spaces = int(n / 2)
    ast = "*"
    res = ""
    if n < 0 or n % 2 == 0:
        return None
    else:
        for i in range(int(n/2) + 1):
            res += " " * spaces + ast + "\n"
            spaces -= 1
            ast += "**"
            if spaces == -1:
                break
        spaces = 0
        ast = ast[2:]
        for i in range(int(n/2)):
            spaces += 1
            ast = ast[2:]
            res += " " * spaces + ast + "\n"
            if spaces == int(n / 2):
                break
        return res

# Teste

print(diamond(5))
print(diamond(9))
print(diamond(35))