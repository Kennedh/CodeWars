"""
Escreva uma função que retorne a contagem de caracteres alfabéticos e dígitos numéricos distintos,
sem distinção entre maiúsculas e minúsculas, que ocorrem mais de uma vez na string de entrada.
Pode-se presumir que a string de entrada contém apenas letras (maiúsculas e minúsculas) e dígitos numéricos.
"""

def duplicate_count(text):
    t = ""
    d = ""
    c = 0
    for l in text:
        l = l.lower()
        if l in t and l not in d:
            c += 1
            d += l
        else:
            t += l
    return c

# Teste

print(duplicate_count("Indivisibilities"))
print(duplicate_count("aaabdcghess"))
