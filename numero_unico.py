"""
Há um array com alguns números. Todos os números são iguais, exceto um. Tente encontrá-lo!
"""

def find_uniq(arr):
    return next(x for x in arr if arr.count(x) == 1)

# Teste

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))