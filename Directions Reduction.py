"""
Remove direções opostas da lista, simplificando o caminho final percorrido.
"""

def dir_reduc(arr):
    opostos = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    stack = []
    for direction in arr:
        if stack and stack[-1] == opostos[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack

# Teste

print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
