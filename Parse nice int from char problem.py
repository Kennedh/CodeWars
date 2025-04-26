"""
Você pergunta a uma menina pequena: "Quantos anos você tem?"
Ela sempre diz "x anos", onde x é um número aleatório entre 0 e 9.

Escreva um programa que retorne a idade da menina (0-9) como um inteiro.

Suponha que a string de entrada do teste seja sempre uma string válida.
Por exemplo, a entrada do teste pode ser "1 ano" ou "5 anos". O primeiro caractere da string é sempre um número.
"""

def get_age(age):
    return int(age[0])

# Teste

print(get_age("2 years old"))