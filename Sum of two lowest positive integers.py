"""Crie uma função que retorne a soma dos dois menores números positivos,
dado um array de no mínimo 4 inteiros positivos. Nenhum número flutuante ou inteiro não positivo será passado.

Por exemplo, quando um array é passado como [19, 5, 42, 2, 77], a saída deve ser 7.

[10, 343445353, 3453445, 3453545353453]deve retornar 3453455."""

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    min2 = max(numbers)

    for num in numbers:
        if num < min2 and num != min1:
            min2 = num
    return min1 + min2

# Teste

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
