"""
Escreva uma função que receba uma sequência de chaves e determine se a ordem das chaves é válida.
Ela deve retornar truese a sequência é válida e falsese é inválida.

Este Kata é semelhante ao Kata de Parênteses Válidos , mas introduz novos caracteres: colchetes []e chaves {}.
Obrigado a @arnedagpela ideia!

Todas as strings de entrada não estarão vazias e consistirão apenas de parênteses, colchetes e chaves: ()[]{}.
"""

def valid_braces(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

# Teste

print(valid_braces("()[]{}"))
print(valid_braces("([{}])"))
print(valid_braces("([)]"))
print(valid_braces("((()))"))
print(valid_braces("{[(])}"))