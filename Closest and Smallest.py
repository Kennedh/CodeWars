"""
Entrada
uma sequência strngde n números positivos (n = 0 ou n >= 2)
Vamos chamar o peso de um número de soma de seus dígitos. Por exemplo, 99terá "peso" 18, 100terá "peso" 1.

Dois números são "próximos" se a diferença entre seus pesos for pequena.

Tarefa:
Para cada número em strngcalcule seu "peso" e então encontre dois números de strngque tenham:

a menor diferença de pesos ou seja que são os mais próximos
com os menores pesos
e com os menores índices (ou classificações, numerados a partir de 0) emstrng
Saída:
uma matriz de duas matrizes, cada submatriz no seguinte formato:
[number-weight, index in strng of the corresponding number, original corresponding number in corda]

ou um par de dois subarrays (Haskell, Clojure, FSharp) ou um array de tuplas (Elixir, C++)

ou um (char*) em C ou uma string em algumas outras linguagens imitando uma matriz de duas submatrizes ou uma string

ou uma matriz em R (2 linhas, 3 colunas, sem nomes de colunas)

As duas submatrizes são classificadas em ordem crescente por seus pesos numéricos se esses pesos forem diferentes,
por seus índices na string se eles tiverem os mesmos pesos.
"""


def closest(strng):
    if not strng:
        return []

    numbers_str = strng.split()
    data = []
    for i, num_str in enumerate(numbers_str):
        weight = sum(int(digit) for digit in num_str)
        data.append({'weight': weight, 'index': i, 'value': int(num_str)})

    data.sort(key=lambda x: x['weight'])

    min_diff = float('inf')
    result_pair = []

    for i in range(len(data) - 1):
        diff = data[i + 1]['weight'] - data[i]['weight']

        if diff < min_diff:
            min_diff = diff
            result_pair = [data[i], data[i + 1]]
        elif diff == min_diff:
            sum_current = data[i]['weight'] + data[i + 1]['weight']
            sum_best = result_pair[0]['weight'] + result_pair[1]['weight']
            if sum_current < sum_best:
                result_pair = [data[i], data[i + 1]]
            elif sum_current == sum_best:
                if data[i]['index'] < result_pair[0]['index']:
                    result_pair = [data[i], data[i + 1]]

    final_output = [
        [result_pair[0]['weight'], result_pair[0]['index'], result_pair[0]['value']],
        [result_pair[1]['weight'], result_pair[1]['index'], result_pair[1]['value']]
    ]

    final_output.sort(key=lambda x: (x[0], x[1]))

    return final_output

# Teste

print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))