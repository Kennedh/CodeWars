"""
Transformar a primeira letra de cada palavra em maiuscula.
"""

def to_jaden_case(string):
    res = ""
    if string == "":
        return ""
    else:
        for w in string.split(" "):
            if res == "":
                res += f"{w[0].upper()+w[1:].lower()}"
            else:
                res += f" {w[0].upper()+w[1:].lower()}"
    return res

# Teste

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))