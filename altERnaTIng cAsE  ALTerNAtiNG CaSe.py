"""
Defina String.prototype.toAlternatingCase(ou uma função/método similar,
como to_alternating_case / toAlternatingCase/ ToAlternatingCaseno idioma selecionado;
veja a solução inicial para mais detalhes ) de forma que cada letra minúscula se torne maiúscula
 e cada letra maiúscula se torne minúscula. Por exemplo:
"""

def to_alternating_case(string):
    res = ""
    for l in string:
        if l.islower():
            res += l.upper()
        else:
            res += l.lower()
    return res

# Teste

print(to_alternating_case("KeNnEdH CuStOdIo"))