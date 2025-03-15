"""
Dada uma sequência de dígitos, você deve substituir qualquer dígito abaixo de 5 por '0' e qualquer dígito 5 e acima por '1'.
Retorna a sequência resultante.
"""

def fake_bin(x):
    re = ""
    for num in x:
        if int(num) < 5:
            re += "0"
        else:
            re += "1"
    return re

# Teste

print(fake_bin("45385593107843568"))
print(fake_bin("509321967506747"))
print(fake_bin("366058562030849490134388085"))
print(fake_bin("15889923"))
print(fake_bin("800857237867"))