"""
Considere um array/lista de ovelhas onde algumas ovelhas podem estar faltando em seus lugares. Precisamos de uma função
que conte o número de ovelhas presentes no array (true significa presente).
"""
def count_sheeps(sheep):
    return sheep.count(True)

# Teste

print(count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]))