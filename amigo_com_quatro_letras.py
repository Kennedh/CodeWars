"""
Faça um programa que filtre uma lista de strings e retorne uma lista com apenas o nome do seu amigo.

Se um nome tem exatamente 4 letras, você pode ter certeza de que ele tem que ser um amigo seu!
Caso contrário, você pode ter certeza de que ele não é...
"""

def friend(x):
    friends = []
    for i in x:
        if len(i) == 4:
            friends.append(i)
    return friends

# Teste

names = ["Sara","James", "John", "Arthur"]

print(friend(names))



