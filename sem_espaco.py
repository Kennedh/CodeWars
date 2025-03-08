"""Escreva uma função que remova os espaços da string e depois retorne a string resultante."""


def no_space(x):
    return "".join(x.split())

# Teste

print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
print(no_space("8aaaaa dddd r     "))