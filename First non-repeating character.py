"""
Escreva uma função chamada first_non_repeating_letter† que recebe uma string de entrada e retorna o primeiro caractere
que não se repete em nenhum lugar da string.

Por exemplo, se for fornecida a entrada 'stress', a função deve retornar 't', já que a letra t só ocorre uma vez na
string, e ocorre primeiro na string.

Como um desafio adicional, letras maiúsculas e minúsculas são consideradas o mesmo caractere , mas a função deve
retornar a caixa correta para a letra inicial. Por exemplo, a entrada 'sTreSS'deve retornar 'T'.

Se uma string contiver todos os caracteres repetidos , ela deverá retornar uma string vazia ( "");

† Observação: a função é chamada firstNonRepeatingLetterpor razões históricas, mas sua função deve manipular qualquer
caractere Unicode.
"""

def first_non_repeating_letter(s):
    counts = {}
    for ch in s:
        k = ch.casefold()
        counts[k] = counts.get(k, 0) + 1
    for ch in s:
        if counts[ch.casefold()] == 1:
            return ch
    return ""

# Teste

print(first_non_repeating_letter('moonmen'))