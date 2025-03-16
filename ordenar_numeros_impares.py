"""
Você receberá um array de números.
Você tem que classificar os números ímpares em ordem crescente, deixando os números pares em suas posições originais.
"""

def sort_array(source_array):
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])

    odd_index = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_numbers[odd_index]
            odd_index += 1

    return source_array

# Teste

print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

