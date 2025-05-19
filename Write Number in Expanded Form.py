"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
"""

def expanded_form(num):
    s = str(num)
    partes = []
    for idx, n in enumerate(s):
        if int(n) != 0:
            zeros = len(s) - idx - 1
            partes.append(n + "0" * zeros)
    return " + ".join(partes)

# Teste

print(expanded_form(12))
print(expanded_form(70304))