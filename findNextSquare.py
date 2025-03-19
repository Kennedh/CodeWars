"""Você pode conhecer alguns quadrados perfeitos bem grandes. Mas e o PRÓXIMO?

Complete o método findNextSquare que encontra o próximo quadrado perfeito integral após o passado como parâmetro.
Lembre-se de que um quadrado perfeito integral é um inteiro n tal que sqrt(n) também é um inteiro.

Se o argumento em si não for um quadrado perfeito, retorne -1 ou um valor vazio como None ou null,
dependendo do seu idioma. Você pode assumir que o argumento é não negativo."""

def find_next_square(sq):
    if not (sq ** 0.5).is_integer():
        return -1
    else:
        return int(((sq ** 0.5) + 1) ** 2)


# Teste

print(find_next_square(121))
