"""
O ácido desoxirribonucleico (DNA) é uma substância química encontrada no núcleo das células e carrega as "instruções"
para o desenvolvimento e funcionamento dos organismos vivos.

Se você quiser saber mais: http://en.wikipedia.org/wiki/DNA

Em sequências de DNA, os símbolos "A" e "T" são complementares um do outro, assim como "C" e "G". Sua função recebe um
lado do DNA (sequência, exceto para Haskell); você precisa retornar o outro lado complementar. A sequência de DNA nunca
está vazia ou não há DNA algum (novamente, exceto para Haskell).
"""

def DNA_strand(dna):
    res = ""
    for l in dna:
        if l.lower() == "a":
            res += "T"
        elif l.lower() == "t":
            res += "A"
        elif l.lower() == "g":
            res += "C"
        elif l.lower() == "c":
            res += "G"
    return res

# Teste

print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))


