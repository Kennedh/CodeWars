"""
Um isograma é uma palavra que não tem letras repetidas, consecutivas ou não consecutivas.
Implemente uma função que determina se uma string que contém apenas letras é um isograma.
Suponha que a string vazia seja um isograma. Ignore maiúsculas e minúsculas.
"""

def is_isogram(w):
    w = w.lower()
    return len(set(w)) == len(w)

#Example

print(is_isogram("Wood"))
print(is_isogram("Dermatoglyphics"))
