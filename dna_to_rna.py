"""
Ácido desoxirribonucleico, DNA é a principal molécula de armazenamento de informações em sistemas biológicos.
É composto de quatro bases de ácido nucleico Guanina ('G'), Citosina ('C'), Adenina ('A') e Timina ('T').

O ácido ribonucleico, RNA, é a principal molécula mensageira nas células.
O RNA difere ligeiramente do DNA em sua estrutura química e não contém Timina. No RNA,
a Timina é substituída por outro ácido nucleico Uracila ('U').

Criar uma função que traduza uma determinada sequência de DNA em RNA.
"""

def dna_to_rna(dna):
    return dna.replace("T", "U")

# Teste

print(dna_to_rna("TTTT"))
print(dna_to_rna("GCAT"))
print(dna_to_rna("GACCGCCGCC"))