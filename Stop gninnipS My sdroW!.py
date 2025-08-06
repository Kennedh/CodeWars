"""
Escreva uma função que receba uma string de uma ou mais palavras e retorne a mesma string, mas com todas as palavras com
cinco ou mais letras invertidas (como o nome deste Kata). As strings passadas serão compostas apenas por letras e
espaços. Espaços serão incluídos apenas quando houver mais de uma palavra.
"""

def spin_words(sentence):
    res = []
    for word in sentence.split():
        if len(word) >= 5:
            res.append(word[-1::-1])
        else:
            res.append(word)
    return " ".join(res)

# Teste

print(spin_words("Hey fellow warriors"))
print(spin_words("This sentence is a sentence"))