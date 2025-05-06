"""
Escreva uma função que, dada uma sequência de texto (possivelmente com pontuação e quebras de linha),
retorne uma matriz das 3 palavras mais frequentes, em ordem decrescente do número de ocorrências.

Suposições:
Uma palavra é uma sequência de letras (A a Z) contendo opcionalmente um ou mais apóstrofos ( ') em ASCII.
Apóstrofos podem aparecer no início, meio ou fim de uma palavra ( 'abc, abc', 'abc', ab'csão todos válidos)
Quaisquer outros caracteres (por exemplo #, \, /, ....) não fazem parte de uma palavra e
devem ser tratados como espaços em branco.
As correspondências não devem diferenciar maiúsculas de minúsculas, e as palavras no resultado devem estar em minúsculas.
Empates podem ser desfeitos arbitrariamente.
Se um texto contiver menos de três palavras exclusivas, as 2 primeiras ou 1 primeira palavras deverão ser retornadas,
ou uma matriz vazia se o texto não contiver nenhuma palavra.
"""
import re

def top_3_words(text):
    res = {}
    text = text.lower()
    text = re.sub(r"[^a-z']+", " ", text)
    text = text.split()
    text = [p for p in text if re.search("[a-z]", p)]
    for t in set(text):
        res[t] = text.count(t)
    f = []
    for c, v in sorted(res.items(), key=lambda x: x[1], reverse=True):
        f.append(c)
    return f[0:3:1]

# Teste

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))