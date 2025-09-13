"""
Dadas duas matrizes de strings a1e a2retornando uma matriz classificada rem ordem lexicográfica das strings a1que são
substrings de strings de a2.

Exemplo 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

retornos["arp", "live", "strong"]

Exemplo 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

retornos[]

Notas:
Arrays são escritos em notação "geral". Consulte "Seus Casos de Teste" para obter exemplos em sua linguagem.
No Shell, bash a1e a2são strings. O retorno é uma string onde as palavras são separadas por vírgulas.
Atenção: Em alguns idiomas rdeve ser sem duplicatas.
"""

def in_array(array1, array2):
    r = []
    for a in array1:
        for b in array2:
            if a in b and a not in r:
                r.append(a)
    r.sort()
    return r

# Teste

print(in_array(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))