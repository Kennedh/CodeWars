"""
Tarefa
Neste Kata simples, sua tarefa é criar uma função que transforma uma string em uma onda mexicana.
Você receberá uma string e deverá retornar um array de strings onde uma letra maiúscula representa uma pessoa em pé.

Regras
1. A string de entrada sempre consistirá em letras minúsculas e espaços, mas pode estar vazia,
nesse caso você deve retornar um array vazio. 2. Se o caractere na string for um espaço em branco,
passe por cima dele como se fosse um assento vazio.
"""

def wave(people):
    res = []
    for idx, l in enumerate(people):
        temp = [c for c in people]
        if l.isalpha():
            temp[idx] = l.upper()
            res.append("".join(temp))
    return res

# Teste

print(wave("hello"))