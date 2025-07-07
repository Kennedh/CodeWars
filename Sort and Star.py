"""
Você receberá uma lista de strings. Você deve classificá-la em ordem alfabética (com diferenciação entre maiúsculas e
minúsculas e com base nos valores ASCII dos caracteres) e, em seguida, retornar o primeiro valor.

O valor retornado deve ser uma string, e ter "***"entre cada uma de suas letras.

Você não deve remover ou adicionar elementos do/para o array.
"""

def two_sort(array):
    res = sorted(array, key=str)
    res = list(res[0])
    return "***".join(res)

# Teste

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]))