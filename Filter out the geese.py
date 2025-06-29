"""
Escreva uma função que receba uma lista de strings como argumento e retorne uma lista filtrada contendo os mesmos
elementos, mas com os "gansos" removidos.

Os gansos são quaisquer strings na seguinte matriz, que é pré-preenchida na sua solução:

  ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
Por exemplo, se esta matriz fosse passada como argumento:

 ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
Sua função retornaria o seguinte array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
Os elementos no array retornado devem estar na mesma ordem que no array inicial passado para sua função, embora com o
"geese" removido. Observe que todas as strings estarão na mesma caixa que as fornecidas, e alguns elementos podem ser
repetidos.
"""

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [w for w in birds if w not in geese]

# Teste

print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))