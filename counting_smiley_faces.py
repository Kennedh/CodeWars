"""
Dado um array (arr) como argumento, complete a função countSmileys que deve retornar o número total de rostos sorridentes.

Regras para um rosto sorridente:

Cada rosto sorridente deve conter um par válido de olhos. Os olhos podem ser marcados como : ou ;
Um rosto sorridente pode ter um nariz, mas não precisa. Os caracteres válidos para um nariz são - ou ~
Cada rosto sorridente deve ter uma boca sorridente que deve ser marcada com ) ou D
Nenhum caractere adicional é permitido, exceto os mencionados.

Exemplos válidos de rosto sorridente: :) :D ;-D :~)
Caras sorridentes inválidas: ;( :> :} :]
"""

def count_smileys(arr):
    smileys = 0
    for s in arr:
        if s == ":)" or s == ":D" or s == ";-D" or s == ":~)" or s == ";~D" or s == ";D" or s == ":-)" or s == ":-D":
            smileys += 1

    return smileys

# Teste

print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))