"""
Mova a primeira letra de cada palavra para o final e adicione "ay" ao final da palavra. Não toque nos sinais de
pontuação.
"""

def pig_it(text):
    res = ""
    for w in text.split():
        if not w.isalpha():
            res += " " + w
            break
        if res == "":
            res += w[1:] + w[0] + "ay"
        else:
            res += " " + w[1:] + w[0] + "ay"
    return res

# Teste



print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))