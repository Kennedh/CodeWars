"""
A ideia principal é contar todos os caracteres presentes em uma string.
Se você tiver uma string como aba, o resultado deverá ser {'a': 2, 'b': 1}.

E se a string estiver vazia? O resultado deve ser um literal de objeto vazio, {}.
"""

def count(s):
    res = {}
    for l in s:
        if l in res:
            res[l] += 1
        else:
            res[l] = 1
    return res

# Teste

print(count('abacaxi'))
print(count('water'))


