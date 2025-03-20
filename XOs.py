"""
Verifique se uma string tem a mesma quantidade de 'x's e 'o's.
O método deve retornar um booleano e não diferenciar maiúsculas de minúsculas. A string pode conter qualquer caractere.
"""

def xo(s):
    return True if s.lower().count("x") == s.lower().count("o") else False

# Teste

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
