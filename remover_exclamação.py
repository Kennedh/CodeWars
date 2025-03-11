"""Escreva a função que remove todos os pontos de exclamação de uma determinada string."""

def remove_exclamation_marks(s):
    return s.replace("!","")

# Teste

print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))