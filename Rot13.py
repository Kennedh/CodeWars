"""
ROT13 é uma cifra de substituição de letras simples que substitui uma letra pela letra 13 depois dela no alfabeto.
ROT13 é um exemplo da cifra de César.

Crie uma função que receba uma string e a retorne cifrada com Rot13.
Se houver números ou caracteres especiais incluídos na string, eles devem ser retornados como estão.
Apenas letras do alfabeto latino/inglês devem ser deslocadas, como na "implementação" original do Rot13.

Observe que usá-lo encodeé considerado trapaça.
"""

def rot13(message):
    res = ""
    amin = "abcdefghijklmnopqrstuvwxyz"
    amax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in message:
        if l in amin:
            if amin.index(l) + 13 > 25:
                res += f"{amin[amin.index(l) + 13 - 26]}"
            else:
                res += f"{amin[amin.index(l) + 13]}"
        elif l in amax:
            if amax.index(l) + 13 > 25:
                res += f"{amax[amax.index(l) + 13 - 26]}"
            else:
                res += f"{amax[amax.index(l) + 13]}"
        else:
            res += l
    return res

# Teste

print(rot13('teSt'))
print(rot13('aA bB zZ 1234 *!?%'))