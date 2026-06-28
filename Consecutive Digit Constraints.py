"""
This kata is based on Project Euler Problem 164

Objective
Write a function that takes a number n and returns the number of n digit numbers (without leading zeros) that no
three consecutive digits have a sum greater than 9

Examples
| n  |  number of numbers
|--------------------------
| 1  |  9 (0 doesn't count)
| 2  | 45
| 3  | 165
Note:
n ranges from 1 to 500
Code length limit = 5000 to avoid hard coded solutions

"""


def number_of_numbers(n):
    if n == 1:
        return 9
    if n == 2:
        return 45

    # dp[a][b] = num de sequenciass de comprimento atual
    # onde os dois ultimos diigitos são a e b
    dp = [[0] * 10 for _ in range(10)]

    # Aqui começa pelos números de 2 digitos
    for a in range(1, 10):  # primeiro dígito não pode ser 0
        for b in range(10):
            dp[a][b] = 1

    # Para cada novo digito adicionado
    for _ in range(2, n):
        new_dp = [[0] * 10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                if dp[a][b] == 0:
                    continue
                # El proximo digito deve sem de acordo com essa equação a + b + c <= 9
                max_c = 9 - a - b
                if max_c >= 0:
                    for c in range(max_c + 1):
                        new_dp[b][c] += dp[a][b]
        dp = new_dp

    # Soma todas as sequencias de n digitos
    return sum(sum(row) for row in dp)

# Teste

print(number_of_numbers(1))
print(number_of_numbers(2))
print(number_of_numbers(3))
print(number_of_numbers(5))
