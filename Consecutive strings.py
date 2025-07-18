"""
Você recebe um array (lista) strarrde strings e um inteiro k.
Sua tarefa é retornar a primeira string mais longa, composta por k strings consecutivas , obtidas no array.

n sendo o comprimento do array de strings, se n = 0ou k > nou k <= 0retornar ""
retornar Nothingem Elm, "nada" em Erlang).

Observação
sequências consecutivas: seguem uma após a outra sem interrupção
"""

def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    else:
        max_str = ""
        for i in range(len(strarr) - k + 1):
            concat = "".join(strarr[i:i + k])
            if len(concat) > len(max_str):
                max_str = concat
        return max_str

# teste

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
