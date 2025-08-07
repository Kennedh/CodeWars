"""
Escreva um método que receba uma matriz de letras consecutivas (crescentes) como entrada e que retorne a letra que falta
na matriz.

Você sempre obterá uma matriz válida. E sempre faltará exatamente uma letra. O comprimento da matriz será sempre de pelo
menos 2.
A matriz sempre conterá letras em apenas um caso.
"""

def find_missing_letter(chars):
    current = [ord(x) for x in chars]
    expected = [x for x in range(ord(chars[0]), ord(chars[-1]) + 1)]
    res = [x for x in expected if x not in current]
    return chr(res[0])


# Teste

print(find_missing_letter(['a','b','c','d','f']))
