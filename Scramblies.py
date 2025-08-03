"""
Complete a função scramble(str1, str2)que retorna truese uma parte dos str1caracteres pode ser reorganizada para
corresponder a str2, caso contrário retorna false.

Notas:

Serão utilizadas apenas letras minúsculas (az). Não serão incluídos sinais de pontuação ou dígitos.
O desempenho precisa ser considerado.
"""

def scramble(s1, s2):
    count = {}
    for l in s1:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    for l in s2:
        if l not in count or count[l] == 0:
            return False
        count[l] -= 1
    return True

# Teste

print(scramble('rkqodlw', 'world'))
print(scramble('katas', 'steak'))
