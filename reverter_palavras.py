"""Complete a função que aceita um parâmetro string e inverte cada palavra na string.
Todos os espaços na string devem ser retidos."""

def reverse_words(text):
    return " ".join(palavra[::-1] for palavra in text.split(" "))

# Teste

print(reverse_words('  double  spaced  words  '))
print(reverse_words('The quick brown fox jumps over the lazy dog.'))

