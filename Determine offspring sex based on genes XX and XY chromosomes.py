"""
Os gametas masculinos ou espermatozoides em humanos e outros mamíferos são heterogaméticos e
contêm um de dois tipos de cromossomos sexuais: X ou Y. Os gametas femininos ou óvulos, por outro lado,
contêm apenas o cromossomo sexual X e são homogaméticos.

O espermatozoide determina o sexo de um indivíduo neste caso.
Se um espermatozoide contendo um cromossomo X fertilizar um óvulo, o zigoto resultante será XX ou feminino.
Se o espermatozoide contiver um cromossomo Y, o zigoto resultante será XY ou masculino.

Determine se o sexo da prole será masculino ou feminino com base no cromossomo X ou Y presente no esperma do macho.

Se o espermatozoide contiver o cromossomo X, retorne "Parabéns! Você vai ter uma filha.";
Se o espermatozoide contiver o cromossomo Y, retorne "Parabéns! Você vai ter um filho.";
"""

def chromosome_check(chromosome):
    return "Congratulations! You're going to have a daughter." if chromosome == "XX" else "Congratulations! You're going to have a son."

# Teste

print(chromosome_check('XY'))
print(chromosome_check('XX'))