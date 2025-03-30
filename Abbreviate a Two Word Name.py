"""
Escreva uma função para converter um nome em iniciais.
Este kata pega estritamente duas palavras com um espaço entre elas.

A saída deve ser duas letras maiúsculas com um ponto separando-as.
"""

def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"

# Teste

print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))