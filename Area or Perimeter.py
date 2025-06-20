"""
Você recebe a lengthárea widthde um polígono de 4 lados. O polígono pode ser um retângulo ou um quadrado.
Se for um quadrado, retorne sua área. Se for um retângulo, retorne seu perímetro.
"""

def area_or_perimeter(l , w):
    return (l + w) * 2 if l != w else l * w

# Teste

print(area_or_perimeter(4, 4))
print(area_or_perimeter(6, 10))