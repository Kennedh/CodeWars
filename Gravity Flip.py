"""
Se você já completou este kata e quer um desafio maior, aqui está a versão 3D

Bob está entediado durante as aulas de física, então ele construiu uma caixa de brinquedos para ajudar a passar o tempo.
A caixa é especial porque tem a capacidade de alterar a gravidade.

Há algumas colunas de cubos de brinquedo na caixa, dispostas em linha. A icoluna -ésima contém a_icubos. Inicialmente,
a gravidade na caixa puxa os cubos para baixo. Quando Bob inverte a gravidade, ela começa a puxar todos os cubos para um
determinado lado da caixa, d, que pode ser ou 'L'( 'R'esquerda ou direita). Abaixo está um exemplo de como uma caixa de
cubos poderia ficar antes e depois da inversão da gravidade.
"""

def flip(d, a):
    return sorted(a) if d == "R" else sorted(a,reverse=True)

# Teste

print(flip('L', [1, 4, 5, 3, 5]))
print(flip('R', [3, 2, 1, 2]))