"""
Complete a solução de modo que ela remova ttodo o texto que segue qualquer um dos marcadores de comentários passados.
Qualquer espaço em branco no final da linha também deve ser removido.

Exemplo:

Dada uma sequência de entrada de:

apples, pears # and bananas
grapes
bananas !apples
A saída esperada seria:

apples, pears
grapes
bananas

"""

def strip_comments(strng, markers):
    res = []
    for linha in strng.splitlines():
        corte = len(linha)
        for m in markers:
            idx = linha.find(m)
            if idx != -1 and idx < corte:
                corte = idx
        res.append(linha[:corte].rstrip())
    return "\n".join(res)

# Teste

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples',['#', '!']))