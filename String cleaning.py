"""
Seu chefe decidiu economizar comprando um software de reconhecimento óptico de caracteres de baixo custo
para digitalizar textos de romances antigos e inseri-los no seu banco de dados.
A princípio, ele parece capturar palavras sem problemas, mas você logo percebe que ele insere muitos números em lugares
aleatórios do texto.

Exemplos (entrada -> saída)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'
Seus colegas de trabalho atarefados estão esperando que você encontre uma solução para pegar esse texto ilegível e
remover todos os números. Seu programa receberá uma string, limpará todos os caracteres numéricos e retornará uma string
com espaçamento e caracteres especiais ~#$%^&!@*():;"'.,?intactos.
"""

def string_clean(s):
    res = ""
    for l in s:
        if l.isalpha() or l in """ ~#$%^&!@*():;"'.,?""":
            res += l
    return res

# Teste

print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))
