"""
A função rgb está incompleta. Complete-a de forma que a passagem de valores decimais RGB resulte em uma representação
hexadecimal. Os valores decimais válidos para RGB vão de 0 a 255. Quaisquer valores fora desse intervalo devem ser
arredondados para o valor válido mais próximo.

Observação: sua resposta deve sempre ter 6 caracteres. A abreviação com 3 não funcionará aqui.
"""


def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return f"{r:02X}{g:02X}{b:02X}"

# Teste

print(rgb(0, 0, 0))
print(rgb(255, 255, 255))
print(rgb(1, 2, 3))