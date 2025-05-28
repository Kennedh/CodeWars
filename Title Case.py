"""
Uma sequência de caracteres é considerada em caixa alta se cada palavra na sequência de caracteres for (a)
escrita em maiúscula (ou seja, apenas a primeira letra da palavra em maiúscula) ou (b) considerada uma exceção e
colocada inteiramente em minúscula, a menos que seja a primeira palavra, que é sempre escrita em maiúscula.

Escreva uma função que converta uma string para maiúsculas e minúsculas,
dada uma lista opcional de exceções (palavras secundárias).
A lista de palavras secundárias será fornecida como uma string com cada palavra separada por um espaço.
Sua função deve ignorar a diferenciação entre maiúsculas e minúsculas da string de palavras secundárias —
ela deve se comportar da mesma maneira mesmo que a diferenciação entre maiúsculas e minúsculas da string de
palavras secundárias seja alterada.

Argumentos (Haskell)
Primeiro argumento : lista delimitada por espaços de palavras secundárias que devem sempre estar em minúsculas,
exceto a primeira palavra na string.
Segundo argumento : a string original a ser convertida.
Argumentos (Outros idiomas)
Primeiro argumento (obrigatório) : a string original a ser convertida.
Segundo argumento (opcional) : lista delimitada por espaços de palavras secundárias que devem sempre ser minúsculas,
exceto a primeira palavra da string. Os testes JavaScript/CoffeeScript serão aprovados undefinedquando este argumento
não for utilizado.
"""

def title_case(title, minor_words=''):
    minor = minor_words.split()
    minor = [w.lower() for w in minor]
    t = title.split()
    res = ""
    for idx, w in enumerate(t):
        if w.lower() in minor and idx != 0:
            res += f" {w.lower()}"
        elif idx == 0:
            res += w.title()
        else:
            res += f" {w.title()}"
    return res

# Teste

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))

