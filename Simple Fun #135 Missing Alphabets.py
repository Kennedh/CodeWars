"""
Dada uma sequência de caracteres sque contém apenas letras a to zminúsculas.

Um conjunto de alfabeto é dado por abcdefghijklmnopqrstuvwxyz.

2 conjuntos de alfabetos significam 2 ou mais alfabetos.

Sua tarefa é encontrar a(s) letra(s) que falta(m). Pode ser necessário exibi-las na ordem de az. É possível que haja
mais de uma letra faltando em mais de um conjunto de alfabetos.

Se a string contiver todas as letras do alfabeto, retorne uma string vazia""

Exemplo
Paras='abcdefghijklmnopqrstuvwxy'

O resultado deve ser'z'

Paras='aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy'

O resultado deve ser'zz'

Paras='abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy'

O resultado deve ser'ayzz'

Paras='codewars'

O resultado deve ser'bfghijklmnpqtuvxyz'

Entrada/Saída
[input]cordas
A(s) sequência(s) fornecida(s) contém(êm) um ou mais conjuntos de alfabetos em letras minúsculas.

[output]uma corda
Encontre as letras contidas em cada alfabeto, mas não na(s) sequência(s). Exiba-as na ordem a-z. Se o alfabeto ausente
for repetido, repita-os como "bbccdd", não como ."bcdbcd"


"""

def missing_alphabets(st):
    temp = 0
    az = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    f = {}
    for l in az:
        c = st.count(l)
        f[l] = c
        if c > temp:
            temp = c
    for t in az:
        if f[t] < temp:
            res += t * (temp - f[t])
    return res

# Teste

print(missing_alphabets('aaab'))