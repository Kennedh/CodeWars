"""
Neste kata, sua tarefa é criar todas as permutações de uma string de entrada não vazia e remover duplicatas,
se presentes.

Crie o máximo de "embaralhamentos" que puder!

Exemplos:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Nota: A ordem das permutações não importa.
"""

def permutations(s):
    if len(s) == 1:
        return [s]

    resultados = []

    for i, char in enumerate(s):
        resto = s[:i] + s[i + 1:]
        sub_permutations = permutations(resto)
        for sub in sub_permutations:
            resultados.append(char + sub)
    return list(set(resultados))

# Teste

print(permutations("abc"))

