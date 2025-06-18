"""
Você receberá um array e um valor limite.
Você deve verificar se todos os valores na matriz estão abaixo ou iguais ao valor limite.
Se estiverem, retorne true. Caso contrário, retorne false.

Você pode assumir que todos os valores na matriz são números.
"""

def small_enough(array, limit):
    for num in array:
        if num > limit:
            return False
    return True

# Teste

print(small_enough([66, 101] ,200))
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100))