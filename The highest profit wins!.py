"""
Escreva uma função que retorne o número mínimo e máximo da lista/matriz fornecida.
"""

def min_max(lst):
    return [min(lst),max(lst)]

# teste

print(min_max([2,3,5,6,7,100]))
print(min_max([20,58,69,74,10]))
print(min_max([876,454,23,1,4]))
