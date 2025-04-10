"""
Sua tarefa é ordenar uma string fornecida. Cada palavra na string conterá um único número.
Este número é a posição que a palavra deve ocupar no resultado.

Observação: Os números podem ser de 1 a 9. Portanto, 1 será a primeira palavra (não 0).

Se a string de entrada estiver vazia, retorne uma string vazia.
As palavras na string de entrada conterão apenas números consecutivos válidos.
"""

def order(sentence):
    dic = {}
    for word in sentence.split():
        for char in word:
            if char.isdigit():
                dic[char] = word
    return " ".join([dic[w] for w in sorted(dic)])

# Teste

print(order("4of Fo1r pe6ople g3ood th5e the2"))