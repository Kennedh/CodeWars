"""
Complete a solução para que a função quebre o camel casing, usando um espaço entre as palavras.
"""

def solution(s):
    res = ""
    for l in s:
        if l.isupper():
            res += " " + l
        else:
            res += l
    return res

# Teste

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))