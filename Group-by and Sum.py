"""
Fundo
Muitas vezes, ao trabalhar com dados tabulares brutos, um objetivo comum é dividir os dados em grupos e realizar uma
agregação como forma de simplificar e extrair conclusões significativas a partir deles. A função de agregação pode ser
qualquer coisa que reduza os dados (soma, média, desvio padrão, etc.). Para os fins deste kata, será sempre a função de
soma.

Tarefa
Defina uma função que aceita dois argumentos, o primeiro sendo uma lista de listas que representam os dados brutos e o
segundo sendo uma lista de índices de colunas.

O valor de retorno deve ser um dicionário cuja chave são os grupos como uma tupla e os valores devem ser uma lista
contendo as somas agregadas.

Exemplo
arr = [
  [1, 6, 2, 10],
  [8, 9, 4, 11],
  [9, 8, 7, 12],
  [1, 6, 3, 20],
]

idx = [0, 1]

group(arr, idx) == {
  (1, 6): [5, 30],      # [2 + 3, 10 + 20]
  (8, 9): [4, 11],
  (9, 8): [7, 12]
}
Explicação
As colunas 0e 1são usadas para agrupamento, portanto as colunas 2e 3serão agregadas
As linhas 0e 3são agrupadas porque têm os mesmos valores nas colunas idx, portanto, as colunas que não fazem parte de
idx são agregadas
Linha 1e 2têm valores diferentes nas colunas idx, portanto, não são agrupados e os resultados agregados serão
simplesmente seus próprios valores nas colunas que não fazem parte deidx
Notas
todas as entradas são válidas
argumentos nunca serão vazios
"""

def group(arr, idx):

    idx = [0, 1]
    groupy = []
    values = []
    dic    = {}


    for linha in arr:

        temp_values = []
        temp_keys = []

        for i, coluna in enumerate(linha):
            if i in idx:
                temp_keys.append(coluna)
            else:
                temp_values.append(coluna)
        groupy.append(temp_keys)
        values.append(temp_values)

    for key, value in zip(groupy, values):
        key = tuple(key)
        if key not in dic:
            dic[key] = value.copy()
        else:
            for i in range(len(value)):
                dic[key][i] = dic[key][i] + value[i]

    return dic

# Teste

print(group([[1,2,3],[1,5,6],[1,8,9]],[0]))