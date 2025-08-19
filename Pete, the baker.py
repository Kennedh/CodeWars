"""
Pete gosta de fazer bolos. Ele tem algumas receitas e ingredientes. Infelizmente, ele não é bom em matemática. Você
pode ajudá-lo a descobrir quantos bolos ele conseguiria fazer considerando suas receitas?

Escreva uma função cakes()que receba a receita (objeto) e os ingredientes disponíveis (também um objeto) e retorne o
número máximo de bolos que Pete consegue assar (inteiro). Para simplificar, não há unidades para as quantidades (por
exemplo, 1 lb de farinha ou 200 g de açúcar são simplesmente 1 ou 200). Ingredientes que não estejam presentes nos
objetos podem ser considerados como 0.
"""

def cakes(recipe, available):
    res = []
    for key, val in recipe.items():
        if key not in available:
            res.append(0)
        else:
            res.append(available[key] // recipe[key])
    return min(res)

# Teste

print(cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))



