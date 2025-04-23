"""
Neste kata, você deve, dada uma sequência, substituir cada letra pela sua posição no alfabeto.

Se algo no texto não for uma carta, ignore e não devolva.
"""

def alphabet_position(text):
    res = ""
    for l in text:
        if l.isalpha():
            if res == "":
                res += str(ord(l.lower()) - ord("a") + 1)
            else:
                res += " " + str(ord(l.lower()) - ord("a") + 1)
    return res

# Teste

print(alphabet_position("The sunset sets at twelve o' clock."))
