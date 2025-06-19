"""
A entrada é uma sequência strde dígitos.
Divida a sequência em pedaços (um pedaço aqui é uma substring da sequência inicial)
de tamanho sz(ignore o último pedaço se seu tamanho for menor que sz).

Se a soma dos dígitos de um bloco for divisível por 2, inverta esse bloco; caso contrário,
gire-o uma posição para a esquerda. Junte esses blocos modificados e retorne o resultado como uma string.

Se

szé <= 0ou se str == ""retornar ""
szé maior (>)que o comprimento, stré impossível pegar um pedaço desse tamanho, szportanto retorne "".
"""

def rev_rot(strng, sz):
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""

    result = []
    for i in range(0, len(strng), sz):
        chunk = strng[i:i + sz]
        if len(chunk) < sz:
            break
        digits_sum = sum(int(d) for d in chunk)
        if digits_sum % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])
    return "".join(result)

# Teste

print(rev_rot("733049910872815764",5))