"""
Um anagrama é o resultado da reorganização das letras de uma palavra para produzir uma nova palavra (veja wikipedia ).

Nota: os anagramas não diferenciam maiúsculas de minúsculas

Complete a função para retornar truese os dois argumentos fornecidos forem anagramas um do outro;
retorne false caso contrário.
"""

def is_anagram(test, original):
    return True if sorted(list(test.lower())) == sorted(list(original.lower())) else False

# Teste

print(is_anagram("foefet", "toffee"))
print(is_anagram("dumble", "bumble"))