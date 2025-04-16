"""
Um pangrama é uma frase que contém todas as letras do alfabeto pelo menos uma vez.
Por exemplo, a frase "A rápida raposa marrom salta sobre o cão preguiçoso" é um pangrama,
pois usa as letras de A a Z pelo menos uma vez (maiúsculas e minúsculas não são relevantes).

Dada uma string, detecta se ela é ou não um pangrama. Retorna True se for, False se não for. Ignora números e pontuação.
"""

def is_pangram(st):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(st.lower())

# Teste

print(is_pangram("How quickly daft jumping zebras vex."))