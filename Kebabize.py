"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters
"""

def kebabize(st):
    st = "".join([l if l.isalpha() else "" for l in st])
    if st == "":
        return ""
    res = st[0].lower()
    for l in st[1:]:
        if l.isupper():
            res += "-" + l.lower()
        else:
            res += l.lower()
    return res


# Teste

print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))
print(kebabize('SOS'))
print(kebabize('42'))