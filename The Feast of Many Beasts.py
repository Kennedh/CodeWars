"""
Todos os animais estão tendo um banquete! Cada animal está trazendo um prato.
Há apenas uma regra: o prato deve começar e terminar com as mesmas letras do nome do animal.
Por exemplo, a garça-azul (great blue heron) está trazendo naan de alho (garlic naan) e o chapim (chickadee)
está trazendo bolo de chocolate (chocolate cake).

Escreva uma função feast que receba o nome do animal e o prato como argumentos
e retorne true ou false para indicar se o animal tem permissão para levar o prato para o banquete.

Suponha que beast e dish sejam sempre strings minúsculas e que cada uma tenha pelo menos duas letras.
beast e dish podem conter hifens e espaços, mas eles não aparecerão no início ou no final da string.
Eles não conterão numerais.
"""

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Teste

print(feast("great blue heron", "garlic naan"))
print(feast("chickadee", "chocolate cake"))
print(feast("brown bear", "bear claw"))

